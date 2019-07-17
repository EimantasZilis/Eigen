import os
from pathlib import Path
from file import extensions

class Directory:
    def __init__(self, path):
        self.path = path
        self.files = []
        self.validate()

    def validate(self):
        """ Validate path. Check if path exists """
        path = Path(self.path)
        if not path.exists():
            raise ValueError('"{}" path does not exist'.format(self.path))

    def get_files(self):
        """ Get all files from directory"""
        for dirpath, dirs, files in os.walk(self.path):
            for filename in files:
                file = File(dirpath, filename)
                if file.is_valid():
                    self.files.append(file)

class File:
    def __init__(self, path, filename):
        self.filename = filename
        self.extension = None
        self.path = path
        self.initialise()

    def initialise(self):
        self.extension = Path(self.filename).suffix

    def reader(self, filename):
        """ Return a file reader based on the extension
        It returns None if a reader for an input file
        is not implemented """
        return extensions.VALID_EXTENSIONS.get(self.extension)

    def is_valid(self):
        """ Validate extension and check
        if it is supported. """
        return self.extension in extensions.VALID_EXTENSIONS.keys()
