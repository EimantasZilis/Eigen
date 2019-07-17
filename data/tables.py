import pandas as pd
from file.management import Directory

class Sentences:
    """ Use file.management.Directory object to
    extract and parse sentences from data files """
    def __init__(self, paths):
        self.paths = paths
        self.df = None
        self.initialise()

    def initialise(self):
        self.init_dataframe()
        self.parse_directories()

    def init_dataframe(self):
        """ Initialise sentences dataframe """
        template = {"Document": [], "Raw": [], "Cleaned": [], "Tokenized": []}
        df = pd.DataFrame(template)
        df.index.name = "ID"
        self.df = df

    def parse_directories(self):
        """ Parse data from each file in directories """
        for path in self.paths:
            try:
                dir = Directory(path)
                for file in dir.get_files():
                    self.parse_file(file)
            except ValueError as error:
                print("Warning: {}".format(error))

    def parse_file(self, file):
        pass
