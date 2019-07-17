import user_input as parser
from file.management import Directory

def main():

    cmd = parser.init_parser()
    if cmd.path:
        folder = Directory(cmd.path[0])
        folder.read_files()


if __name__ == "__main__":
    main()
