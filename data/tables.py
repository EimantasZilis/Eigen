import pandas as pd
from file.management import Directory

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
            self.files.append(file)
