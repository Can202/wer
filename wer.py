
#!/usr/bin/python3

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
        if os.path.isfile(pathfile) == True:
            print (read_file(pathfile))
        else:
            print( "Is a Folder")
    else:
        print("your file does not exists")

def impread(path):
    if os.path.exists(path):
        if os.path.isdir(path):
            return read_file(path)
        else:
            return "Is a Folder"
    else:
        return "your file does not exists"



def extra_commands(arg):
    if arg == "-h" or arg == "--help":
        print("wer is a program to read file with terminal")
        print("Use:")
        print("    -h or --help           help")
        print()
        print("    -v or --version        see version")
        print()
        print("    -f or --file-exists    see if the file exists")
        print("      Use:")
        print("        -f <path>")
        print()
        print("    -c or --create-file    create file if it doesn't exist")
        print("      Use:")
        print("        -c <path>")
        exit()
    elif arg == "-v" or arg == "--version":
        print("0.3")
        exit()
    elif arg == "-f" or arg == "--file-exists":
        if len(sys.argv) > 2:
            if file_exists(str(sys.argv[2])) == True:
                print(str(sys.argv[2]) + " exists")
            else:
                print("Not exists")
        else:
            print("-f or --file-exists    see if the file exists")
            print("  Use:")
            print("    -f <path>")
        exit()
    elif arg == "-c" or arg == "--create-file":
        if len(sys.argv) > 2:
            creating = createfile(sys.argv[2])
            if creating == "isfolder":
                print("cannot create folders")
            elif creating == "fileexists":
                print("The File exists")
            elif creating == "folderdoesnotexist":
                print("Folder doesn't exist")

        else:
            print("    -c or --create-file    create file if it doesn't exist")
            print("      Use:")
            print("        -c <path>")
        exit()


def createfile(path):
    arg2 = str(path)

    if arg2.endswith("/") or arg2.endswith("\\"):
        return "isfolder"
    if file_exists(arg2):
        return "fileexists"
    if folder_exists(arg2) == False:
        return "folderdoesnotexist"

    fp = open(arg2, 'x')
    fp.close()
    return "done"



def folder_exists(pathfile):
    name = os.path.basename(pathfile)

    path = pathfile.replace(name,"")


    if os.path.exists(path):
        return True
    else:
        return False

def file_exists(pathfile):
    if os.path.exists(pathfile):
        return True
    else:
        return False

def read_file(pathfile):
    file = open(pathfile,'r', encoding='utf8')
    contents = file.read()
    return contents


if __name__ == '__main__':
    main()

