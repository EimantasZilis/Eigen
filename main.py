import argparse
import data.tables

def cmd_parser():
    """ Initialise and define user input commands """
    parser = argparse.ArgumentParser(description='Create hashtags')
    parser.add_argument("-p", nargs="+", dest="path", help="Enter path. \
                        It finds all files within and generates hashtags")
    return parser.parse_args()

def main():
    cmd = cmd_parser()
    if cmd.path:
        sentences = data.tables.Sentences(cmd.path)

if __name__ == "__main__":
    main()
