import os
from nltk.corpus import stopwords
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
            if sent:
                ok_words.append(sent)
        file.words = ok_words
