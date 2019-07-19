from pathlib import Path

""" Module specifies valid extensions for reading data.
Each valid extension is represented by a class. For any
new filetypes, a class must be defined and a mapping
added to VALID_EXTENSIONS"""

class Txt:
    """ Class for reading .txt files """
    def __init__(self, filepath):
        self.filepath = filepath
        self.raw = None
        self.read()

    def read(self):
        try:
            with open(self.filepath, "r", encoding="utf8") as file:
                data = file.readlines()
                if data:
                    self.raw = data
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
        # Not implemented
        pass

class Docx:
    """ Class for reading .docx files.
    It is currently not implemented """
    def __init__(self, filepath):
        self.filepath = filepath
        self.raw = None
        self.read()

    def read(self):
        # Not implemented
        pass


VALID_EXTENSIONS = {".txt": Txt, ".pdf": Pdf, ".docx": Docx}
