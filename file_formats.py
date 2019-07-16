
""" Specifies compatible file formats. Use appropriate
classes to extract raw text from relevant file format. """

class Txt:
    """ Class for reading .txt files """
    def __init__(self, filepath):
        self.filepath = filepath
        self.raw = None
        self.read()

    def read(self):
        try:
            with open(self.filepath, "r") as file:
                self.raw = file.readlines()
        except FileNotFoundError:
            pass

class Pdf:
    """ Class for reading .pdf files.
    It is currently not implemented """
    def __init__(self, filepath):
        self.filepath = filepath
        self.raw = None
        self.read()

    def read(self):
        pass

class Docx:
    """ Class for reading .docx files.
    It is currently not implemented """
    def __init__(self, filepath):
        self.filepath = filepath
        self.raw = None
        self.read()

    def read(self):
        pass
