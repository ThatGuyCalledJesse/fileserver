# OS is used to list all files in the directory
import os


# This function takes all files in a directory and removes them one by one
def clear_files() -> str:
    # Set the 'folder' variable to uploads, which is the folder where our files are being stored
    folder = 'uploads'
    # Make a list called 'files' and store all files in the directory in that variable
    files = os.listdir(folder)
    # For every file in the list
    for file in files:
        # Remove the file from the folder
        os.remove(f'{folder}/{file}')
    # Then return a message saying that all files are removed
