import argparse

def init_parser():
    """ Initialise and define user input commands """
    parser = argparse.ArgumentParser(description='Create hashtags')
    parser.add_argument("-p", nargs="+", dest="path", help="Enter path. \
                        It finds all files within and generates hashtags")
    return parser.parse_args()
