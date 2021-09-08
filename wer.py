
import sys
from sys import exit
import os

def main():

    if len(sys.argv) > 1:
        pathfile = sys.argv[1]
        pathfile = str(pathfile)
    else:
        extra_commands("-h")
        exit()

    extra_commands(pathfile)

    if os.path.exists(pathfile):
        read_file(pathfile)
    else:
        print("your file does not exists")


def extra_commands(arg):
    if arg == "-h" or arg == "--help":
        print("wer is a program to read file with terminal")
        print("Use:")
        print("    -h or --help           help")
        print("    -v or --version        see version")
        print("    -f or --file-exists    see if the file exists")
        print("      Use:")
        print("        -f <path>")
        exit()
    elif arg == "-v" or arg == "--version":
        print("0.1-dev")
        exit()
    elif arg == "-f" or arg == "--file-exists":
        if len(sys.argv) > 2:
            file_exists(str(sys.argv[2]))
        else:
            print("-f or --file-exists    see if the file exists")
            print("  Use:")
            print("    -f <path>")
        exit()

def file_exists(pathfile):
    if os.path.exists(pathfile):
        print(pathfile + " exists")
    else:
        print("Not exists")

def read_file(pathfile):
    file = open(pathfile,'r', encoding='utf8')
    contents = file.read()
    print(contents)


if __name__ == '__main__':
    main()

