This is a step-by-step documentation on how I built FileServer.
# Planning
First I opened the Ubuntu text editor and started writing down some ideas, the best idea was the file server.
Then I wrote down what packages would be required for a program like this (os, werkzeus.utils and flask).
# Coding
Then I started writing the code, first the imports (I added 1 extra function to remove all files from the server).
Then I made a `send_from_directory` function that returns a file to an HTTP request.
```import os
from flask import send_file

def send_from_directory(directory: str, filename: str):
    # I struggled to remove the file from the system at first, but then decided to use this approach
    file = send_file(os.path.join(directory, filename), as_attachment=True)
    os.system(f'rm uploads/{filename}')
    return file
```
And now I could return files to HTTP requests.
Then I made the flask app and wrote the functions for the routes, implemented the `send_from_directory` function in the download_file route,
added the upload route and added a button to remove all files from the server.
Then I got a pull request for a change that would make it easier to use, it got merged and I wrote some more commits myself.
Then I got another pull request for a CSS change that would beautify things (and it did).
# Automation
To make FileServer easier to use I added two files, `start_server.sh` and `start_server.bat`,
these files are used to run the program without having to set anything up yourself.
If there is no venv found in the working directory the program will create it and install the required packages.
# Resources
I used Google and `chat.openai.com` for some code snippets.
# Recap
Overall I would say this is a fun project to make, it took around half a day for the initial project, 
but the entire project took a few weeks, but in the end it is done and I learned some new skills.
