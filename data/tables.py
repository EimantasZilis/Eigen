import pandas as pd
from file.management import Directory
from nltk.tokenize import sent_tokenize
from nltk.tokenize import word_tokenize

class Sentences:
    """ Use file.management.Directory object to
    extract and parse sentences from data files """
    def __init__(self, paths):
        self.paths = paths
        self.files = []
        self.initialise()

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
        for file in dir.get_files():
            self.tokenize_data(file)
            self.files.append(file)

    def tokenize_data(self, file):
        """ Tokenize data in file"""
        self.tokenize_sentences(file)
        self.tokenize_words(file)

    @staticmethod
    def tokenize_sentences(file):
        """ Split text by sentences """
        fsentences = []
        for line in file.data:
            fsentences.extend(sent_tokenize(line))
        file.sentences = fsentences

    @staticmethod
    def tokenize_words(file):
        twords = []
        for fsentence in file.sentences:
            twords.append(word_tokenize(fsentence))
        file.words = twords
