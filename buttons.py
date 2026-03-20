# This part is incredibly primitive, but it works so I never really rewrote it. Maybe someday I'll try a more orthodox approach, when this inevitably breaks perhaps.

# This function takes a list of strings (files) and adds HTML code for a button for every file when download is called
def create_buttons(files: list[str]):
    # Only execute this code block if there are files in the list
    if len(files) != 0:
        html_string = "" # This is the string that will hold the html the the page render
        for file in files: # For each files in the list
            # Add a button with the value and name set to the name of the file
            html_string += f"""
            <form method=post enctype=multipart/form-data>
            <input type=submit value="{file}" name="{file}">
            </form>\n"""
        # When finished return the string
        return html_string
    # Else return a message saying that there are no files
    else:
        return '<h1>There are no files upload, go to <a href="/upload">/upload</a> and upload some files.'
