import os
from pathlib import Path
from file import extensions

class Directory:
    def __init__(self, path):
        self.path = path
        self.validate()

    def validate(self):
        """ Validate path. Check if path exists """
        path = Path(self.path)
        if not path.exists():
            raise ValueError('"{}" path does not exist'.format(self.path))

    def get_files(self):
        """ Get all files from directory and its sub folders
        and read them"""
        for dirpath, dirs, files in os.walk(self.path):
            for filename in files:
                file = File(dirpath, filename)
                if file.is_valid():
                    file.read()
                    if file.raw is not None:
                        yield file

class File:
    def __init__(self, path, filename):
        self.filename = filename
        self.extension = None
        self.path = path
        self.raw = None
        self.sentences = None
        self.words = None
        self.initialise()

    def initialise(self):
        self.extension = Path(self.filename).suffix

    def read(self):
        file_reader = self.reader()
        full_path = self.full_path()
        freader = file_reader(full_path)
        self.raw = freader.raw

    def reader(self):
        """ Return a file reader based on the extension
        It returns None if a reader for an input file
        is not implemented """
        return extensions.VALID_EXTENSIONS.get(self.extension)

    def is_valid(self):
        """ Validate extension and check
        if it is supported. """
        return self.extension in extensions.VALID_EXTENSIONS.keys()

    def full_path(self):
        return os.path.join(self.path, self.filename)
