import os
import sys
import time

def show_directories_tree():
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


def create_directories():
    parent_dir = "../"

    new_file = os.path.join(parent_dir, "Desktop aShotcuttttttttttttt")
    os.mkdir(new_file)

    new_file = os.path.join(new_file, "Desktop")
    os.mkdir(new_file)

    desktop_root = ["Drives And Tools", "Edition-Creation", "Games", "Programming", "Utils"]

    current_root = new_file
    for file in desktop_root:
        new_file = os.path.join(current_root, file)
        os.mkdir(new_file)

    games_root = ["4Fun", "Platforms", "Story"]

    current_root = os.path.join(current_root, "Games")
    for file in games_root:
        new_file = os.path.join(current_root, file)
        os.mkdir(new_file)

    print("Folders created as expected")


def install_programs(file_name):
    if (os.path.exists(file_name)):
        with open("download.txt", "r") as f:
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



if (sys.argv[1] == "-a" or sys.argv[1] == "--all"):
    print(
    """You've selected a COMPLETE instalation process.
    This mean all the programs set on download file will be installed
    Also, the directories will be created.
    Any doubts, read the readme.md file that should be located along with this script."""
    )
    time.sleep(5)

    show_directories_tree()
    create_directories()
    install_programs()

elif (sys.argv[1] == "-d" or sys.argv[1] == "--directories"):
    print(
    """You've selected ONLY DIRECTORIES creation.
    This mean that all the directories will be created.
    Any doubts, read the readme.md file that should be located along with this script."""
    )
    time.sleep(5)

    show_directories_tree()
    create_directories()

else:
    print(
    """You've selected a DEFAULT installation. 
    All the programs set on download will be installed
    Any doubts, read the readme.md file that should be located along with this script."""
    )
    time.sleep(5)

    install_programs()
    