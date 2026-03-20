import os


def clear_files() -> str: # Function must return a string
    # Set the 'folder' variable to uploads, which is the folder where our files are being stored
    folder = 'uploads'
    files = os.listdir(folder) # A list to store all listed files as a variable
    # For every file in the list
    for file in files:
        # Remove the file from the folder
        os.remove(f'{folder}/{file}')
