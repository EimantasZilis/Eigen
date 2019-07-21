import os
from collections import defaultdict
import sys

from nltk.corpus import stopwords
from nltk.probability import FreqDist
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize
from nltk.stem.wordnet import WordNetLemmatizer
import pandas as pd

from file.management import Directory

STOP_WORDS = set(stopwords.words('english'))
LEM = WordNetLemmatizer()

class Text:
    """ Checks all input paths, gets all files, subfolders,
    import the data from supported files and cleans it. It
    removes stopwords and lemmatizes words """

    def __init__(self, paths):
        self.freq_dist = None
        self.all_words = []
        self.paths = paths
        self.files = []

    def initialise(self):
        self.import_data()

    def import_data(self):
        """ Read and import data from all files from paths attribute
        and its subfolders """
        for path in self.paths:
            try:
                self.check_directory(path)
            except ValueError as error:
                print("Warning: {}".format(error))

    def check_directory(self, path):
        """ Check directory and process files within"""
        dir = Directory(path)
        print("Reading data files...")
        for file in dir.get_files():
            print(" >> {}".format(os.path.join(path, file.filename)))
            self.files.append(file)

    def clean(self):
        """ Clean data by tokenizing words and sentences,
        removing stop words, lematizing words and applying
        other processing """
        print("Cleaning data...")
        for file in self.files:
            self.tokenize_sentences(file)
            self.tokenize_words(file)
            self.remove_stopwords(file)
            self.apply_lematizing(file)
            self.other_processing(file)

    @staticmethod
    def tokenize_sentences(file):
        """ Split text by sentences """
        fsentences = []
        for line in file.raw:
            fsentences.extend(sent_tokenize(line))
        file.sentences = fsentences

    @staticmethod
    def tokenize_words(file):
        file.words = [word_tokenize(words) for words in file.sentences]

    @staticmethod
    def remove_stopwords(file):
        """ Strip away stopwords from words attribute in file"""
        file.words = [[w.lower() for w in words if w.lower() not in STOP_WORDS]
                       for words in file.words]
    @staticmethod
    def apply_lematizing(file):
        """ Reduces words to their word root word
        or chops off the derivational affixes"""
        file.words = [[LEM.lemmatize(w, "v") for w in words]
                       for words in file.words]

    @staticmethod
    def other_processing(file):
        """ Remove the following words:
        1) Single character words
        2) Remove words that start with non-alphanumberic
        characters. These have most likely originated from
        incorrect tokenization, leaving bad words like
        "'ve", etc.
        3) Remove "n't" words. The have most likely come
        from tokenization. """

        ok_words = []
        for words in file.words:
            sent = [w for w in words
                    if len(w) > 1 if w[0].isalpha() if w != "n't"]
            ok_words.append(sent)
        file.words = ok_words

    def analyse(self):
        """ Analyse text and work out frequency distribution """
        self.get_all_words()
        self.get_frequency_distribution()

    def get_all_words(self):
        """ Get all words across files and put
        it in a single list"""
        for file in self.files:
            for sentences in file.words:
                self.all_words.extend(sentences)

    def get_frequency_distribution(self):
        """ Generate frequency distribution"""
        self.freq_dist = FreqDist(self.all_words)

    def most_common_words(self, n):
        """ Generate n number of most commonly used words"""
        words_frequencies = self.freq_dist.most_common(n)
        return words_frequencies

class Output:
    """ Generate output, summarizing most common
    words and sentences in which they occur"""
    def __init__(self, data, common_words):
        self.common_words = common_words
        self.data = data
        self.df = None
        self.initialise()

    def initialise(self):
        print("Generating output...")
        data_output = self.init_data()
        self.init_dataframe(data_output)
        self.excel()

    def init_data(self):
        """ Prepare data to be inserted into dataframe"""
        data_output = defaultdict(list)
        for cword, frequency in self.common_words:
            for file in self.data.files:
                for sid in range(len(file.words)):
                    if cword in file.words[sid]:
                        sent = file.sentences[sid]
                        file_path = os.path.join(file.path, file.filename)
                        data_output["Word (#)"].append(cword)
                        data_output["Frequency"].append(frequency)
                        data_output["Document"].append(file_path)
                        data_output["Sentence containing the word"].append(sent)
        return data_output

    def init_dataframe(self, data_output):
        """ Initialise dataframe with data"""
        self.df = pd.DataFrame(data_output)

    def excel(self):
        """ Generate CSV output"""
        self.df.to_csv(r"C:\Users\Eimantas\Desktop\output.csv", index=False)
