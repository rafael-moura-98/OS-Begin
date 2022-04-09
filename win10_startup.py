import os
import sys
import time


def show_directories_tree():
    """ A simple function to show the user all the directories
    that will be created"""

    print("""
    An desktop tree folders will be created as follow: 
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
        print(f"Didn't created {path}. A file with this name\
             already exists in this directory.")


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

    print("Folders creation ran as expected")


def install_programs(file_name):
    """ Install all programs listed on file_name"""
    if (os.path.exists(file_name)):
        with open(file_name, "r") as f:
            download = f.read().splitlines()
    
    else:
        print("A file named {file_name} couldn't be found. Exiting...")
        exit()

    print("""
    #################################################
    The following programs are about to be installed:
    """)

    for program in download:
        print(f"#{program}")
    
    print("""
    #################################################
    
    The installation process will start in 10 seconds.

    Press CTRL + C if you want to cancel.
    """
    )

    time.sleep(10)

    # Install all files
    for program in download:
        os.system(f'choco install {program}')


## Main

if len(sys.argv) == 2:        # If one parameter is passed
    if (sys.argv[1] == "-a" or sys.argv[1] == "--all"):
        print(
        """You've selected a COMPLETE instalation process.
        This mean all the programs written on download.txt will be installed.
        Also, the directories will be created.
        Any doubts, read the readme.md file that should be located along\
             with this script."""
        )
        time.sleep(5)

        show_directories_tree()
        create_directories()
        install_programs("download.txt")

    elif (sys.argv[1] == "-d" or sys.argv[1] == "--directories"):
        print(
        """You've selected ONLY DIRECTORIES creation.
        This mean that all the directories will be created.
        Any doubts, read the readme.md file that should be located along with\
             this script."""
        )
        time.sleep(5)

        show_directories_tree()
        create_directories()
    
    else:
        print("Unexpected set of pararameter on call. Exiting...")
        exit()

elif len(sys.argv) == 1:        # If none parameter is passed
    print(
    """You've selected a DEFAULT installation. 
    All the programs set on download will be installed
    Any doubts, read the readme.md file that should be located along with \
        this script."""
    )
    time.sleep(5)

    install_programs("download.txt")
    