import user_input as parser
from file.management import Directory

def main():

    cmd = parser.init_parser()
    if cmd.path:
        dir_path = Directory(cmd.path[0])
        dir_path.get_files()


if __name__ == "__main__":
    main()
