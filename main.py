import argparse
import data
from nltk import download

def cmd_parser():
    """ Initialise and define user input commands """
    parser = argparse.ArgumentParser(description='Create hashtags')
    parser.add_argument("-i",  action="store_true", default=False, dest="install",
                        help="Install relevant nltk packages")
    parser.add_argument("-p", nargs="+", dest="paths", help="Enter paths. \
                        It will find all files within and generates hashtags")
    return parser.parse_args()

def main():
    cmd = cmd_parser()
    if cmd.install:
        print("Installing nltk packages...")
        download('punkt')
        download('stopwords')
        download('wordnet')

    if cmd.paths:
        text = data.Text(cmd.paths)
        text.import_data()
        text.clean()
        text.analyse()
        common_words = text.most_common_words(20)
        data.Output(text, common_words)

if __name__ == "__main__":
    main()
