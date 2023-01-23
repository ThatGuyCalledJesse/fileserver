from flask import Flask, render_template

# This function takes a list[str] of files and adds HTML code for a button for every file when download is called
def create_buttons(files: list[str]):
    # Only execute this code block if there are files in the list
    if len(files) != 0:
        return render_template("download.html", files=files)
    else:
        return '<h1>There are no files upload, go to <a href="/upload">/upload</a> and upload some files.'