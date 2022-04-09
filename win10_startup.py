import os
import sys
import time


GREEN='\033[32m'
ORANGE='\033[33m'
YELLOW='\033[93m'
RED='\033[31m'
ENDC='\033[0m'


def show_directories_tree():
    """ A simple function to show the user all the directories
    that will be created"""

    print(f"""
    {ORANGE}An desktop tree folders will be created as follow:{ENDC} 
    └───Desktop
        ├───Drives And Tools
        ├───Edition-Creation
        ├───Games
        │   ├───4Fun
        │   ├───Platforms
        │   └───Story
        ├───Programming
        └───Utils
        """)


def make_directory(path):
    if not os.path.exists(path):
        os.mkdir(path)
    else:
        print(f"{YELLOW}Didn't created \"{path}\". A file with this"
             f" name already exists in this directory.{ENDC}")


def create_directories():
    """ Create a tree of directories """

    parent_dir = "../"

    new_file = os.path.join(parent_dir, "Desktop Shortcuts")
    make_directory(new_file)

    new_file = os.path.join(new_file, "Desktop")
    make_directory(new_file)

    desktop_root = ["Drives And Tools", "Edition-Creation", "Games",
     "Programming", "Utils"]

    current_root = new_file
    for file in desktop_root:
        new_file = os.path.join(current_root, file)
        make_directory(new_file)

    games_root = ["4Fun", "Platforms", "Story"]

    current_root = os.path.join(current_root, "Games")
    for file in games_root:
        new_file = os.path.join(current_root, file)
        make_directory(new_file)

    print(f"{GREEN}Folders creation ran as expected{ENDC}")


def install_programs(file_name):
    """ Install all programs listed on file_name"""
    if (os.path.exists(file_name)):
        with open(file_name, "r") as f:
            download = f.read().splitlines()
    
    else:
        print(f"{RED}Can't download programs. A file named {file_name}"
             f" couldn't be found. Exiting...{ENDC}")
        exit()

    print(f"""
    {ORANGE}#################################################
    The following programs are about to be installed:{ENDC}
    """)

    for program in download:
        if not "#" in program:
            print(f"{ORANGE}#{ENDC}{program}")
    
    print(f"""
    {ORANGE}#################################################{ENDC}
    
    {YELLOW}The installation process will start in 10 seconds.

    Press CTRL + C if you want to cancel.{ENDC}
    """
    )

    if not download:
        print("Just kidding! You selected nothing... Exiting")
        time.sleep(3)
        print(f"{RED}Empty file. download.txt doesn't contain any program name.{ENDC}")
        exit()

    time.sleep(10)

    # Install all files
    for program in download:
        if not "#" in program:
            os.system(f'choco install {program} -y')


## Main

if len(sys.argv) == 2:        # If one parameter is passed
    if (sys.argv[1] == "-a" or sys.argv[1] == "--all"):
        print(
        f"{ORANGE}You've selected a COMPLETE instalation process.{ENDC}\n"
        "This mean all the programs written on download.txt will be installed.\n"
        "Also, the directories will be created.\n"
        "Any doubts, read the readme.md file that should be located along"
            " with this script.\n"
        )
        time.sleep(10)

        show_directories_tree()
        create_directories()
        install_programs("download.txt")

    elif (sys.argv[1] == "-d" or sys.argv[1] == "--directories"):
        print(
        f"{ORANGE}You've selected ONLY DIRECTORIES creation.{ENDC}\n"
        "This mean that all the directories will be created.\n"
        "Any doubts, read the readme.md file that should be located"
            " along with this script.\n"
        )
        time.sleep(10)

        show_directories_tree()
        create_directories()
    
    else:
        print(f"{RED}Unexpected set of pararameter on call. Exiting...{ENDC}")
        exit()


elif len(sys.argv) == 1:        # If none parameter is passed
    print(
    f"{ORANGE}You've selected a DEFAULT installation.{ENDC}\n"
    "All the programs set on download will be installed.\n"
    "Any doubts, read the readme.md file that should be located along with"
        " this script.\n"
    )
    time.sleep(10)

    install_programs("download.txt")
    