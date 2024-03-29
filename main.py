import argparse
import os.path
import data
from nltk import download

def cmd_parser():
    """ Initialise and define user input commands """
    parser = argparse.ArgumentParser(description='Create hashtags')
    parser.add_argument("-i", "--INSTALL", action="store_true", default=False,
                        dest="install", help="Install relevant nltk packages")
    parser.add_argument("-c", "--COUNT", dest="count", type=int, default=20,
                        help="Set the number of most common words to return. \
                        Default: 20")
    parser.add_argument("-o", "--OUTPUT", nargs="+", dest="output", help="Set \
                        directory for output CSV. Default path is user desktop.")
    parser.add_argument("-p", "--PATHS", nargs="+", dest="paths", help="Enter \
                        paths. It will find all files and generates hashtags")
    return parser.parse_args()

def main():
    cmd = cmd_parser()
    if cmd.install:
        print("Installing nltk packages...")
        download('punkt')
        download('stopwords')
        download('wordnet')

    if cmd.output:
        output_path = cmd.output[0]
    else:
        output_path = os.path.expanduser("~\\Desktop")

    if cmd.paths:
        text = data.Text(cmd.paths)
        text.import_data()
        text.clean()
        text.analyse()
        common_words = text.most_common_words(cmd.count)
        data.Output(text, common_words, output_path)

if __name__ == "__main__":
    main()
