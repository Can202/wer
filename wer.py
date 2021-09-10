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

    for i in range(len(sys.argv) - 1):
        temparg = i + 1

        if os.path.exists(sys.argv[temparg]):
            if os.path.isfile(sys.argv[temparg]) == True:
                print(read_file(sys.argv[temparg]))
            else:
                print("Is a Folder")
        else:
            print("your file does not exists")

def impread(path):
    if os.path.exists(path):
        if os.path.isfile(path):
            return read_file(path)
        else:
            return "Is a Folder"
    else:
        return "your file does not exists"

def listdir(path):
    print(os.listdir(path))

def extra_commands(arg):
    if arg == "-h" or arg == "--help":
        print("wer is a program to read file with terminal")
        print("Use:")
        print("  Normal:")
        print("    wer <path>             read the file")
        print()
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
        print()
        print("    -w or --write-file    Create a file, and write to a file")
        print("      Use:")
        print("        -w <path> \"<text>\"")
        print()
        print("    -a or --add-file    Add text to a file")
        print("      Use:")
        print("        -a <path> \"<text>\"")
        print()
        print("    -l or --list-dir    list directory")
        print("      Use:")
        print("        -l          list current directory")
        print("        -l <path>   list <path> directory")
        print()
        print("    -rm or --remove     remove file")
        print("      Use:")
        print("        -rm <path>")
        print()
        print("    -cc or --clear-console     clear console")
        exit()
    elif arg == "-v" or arg == "--version":
        print("0.5")
        exit()
    elif arg == "-f" or arg == "--file-exists":
        if len(sys.argv) > 2:
            if file_exists(str(sys.argv[2])) == True:
                print(str(sys.argv[2]) + " exists")
            else:
                print("Not exists")
        else:
            print("-f or --file-exists    See if the file exists")
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
            print("    -c or --create-file    Create file if it doesn't exist")
            print("      Use:")
            print("        -c <path>")
        exit()

    elif arg == "-w" or arg == "--write-file":
        if len(sys.argv) > 3:
            text=str(sys.argv[3])
            creating = createfile(sys.argv[2], write='w', text=text)
            if creating == "isfolder":
                print("cannot create folders")
            elif creating == "fileexists":
                print("The File exists")
            elif creating == "folderdoesnotexist":
                print("Folder doesn't exist")

        else:
            print("    -w or --write-file    Create a file, and write to a file")
            print("      Use:")
            print("        -w <path> \"<text>\"")
        exit()

    elif arg == "-a" or arg == "--add-file":
        if len(sys.argv) > 3:
            text=str(sys.argv[3])
            creating = createfile(sys.argv[2], write='a', text=text)
            if creating == "isfolder":
                print("cannot create folders")
            elif creating == "fileexists":
                print("The File exists")
            elif creating == "folderdoesnotexist":
                print("Folder doesn't exist")

        else:
            print("    -a or --add-file    Add text to a file")
            print("      Use:")
            print("        -a <path> \"<text>\"")
        exit()
    elif arg == "-l" or arg == "--list-dir":
        if len(sys.argv) > 2:
            patha = str(sys.argv[2])
            if os.path.isdir(patha):
                ls = os.listdir(patha)
            else:
                ls = os.listdir(patha.replace(os.path.basename(patha), ""))
        else:
            ls = os.listdir('.')
        i = 0
        for i in range (len(ls)):
            print("- " + ls[i])
        exit()
    elif arg == "-rm" or arg == "--remove":
        if len(sys.argv) > 2:
            patha = str(sys.argv[2])
            if os.path.exists(patha):
                if os.path.isfile(patha):
                    os.remove(patha)
                    exit()
                else:
                    print("not file")
                    exit()
            else:
                print("the file doesn't exist")
                exit()
        else:
            print("    -rm or --remove     remove file")
            print("      Use:")
            print("        -rm <path>")
            exit()
    elif arg == "-cc" or arg == "--clear-console":
        os.system('clear||cls')
        exit()



def createfile(path, write='x', text=""):
    arg2 = str(path)

    if arg2.endswith("/") or arg2.endswith("\\"):
        return "isfolder"

    if file_exists(arg2):
        if write == 'x':
            return "fileexists"

    if folder_exists(arg2) == False:
        return "folderdoesnotexist"

    fp = open(arg2, write)
    if write != 'x':
        fp.write(str(text))

    fp.close()
    return "done"



def folder_exists(pathfile):
    if "/" in pathfile or "\\" in pathfile:
        name = os.path.basename(pathfile)

        path = pathfile.replace(name,"")


        if os.path.exists(path):
            return True
        else:
            return False
    return True

def file_exists(pathfile):
    if os.path.exists(pathfile):
        return True
    else:
        return False

def read_file(pathfile):
    file = open(pathfile,'r', errors="ignore", encoding='utf8')
    contents = file.read()
    return contents


if __name__ == '__main__':
    main()

