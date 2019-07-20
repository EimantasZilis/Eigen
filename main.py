import argparse
import data
import nltk

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
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')

    if cmd.paths:
        text = data.Text(cmd.paths)
        text.import_data()
        text.clean()

if __name__ == "__main__":
    main()
