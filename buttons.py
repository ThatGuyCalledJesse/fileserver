# This function takes a list[str] of files and adds HTML code for a button for every file when download is called
def create_buttons(files: list[str]):
    # Only execute this code block if there are files in the list
    if len(files) != 0:
        # Empty string that represents an HTML file
        html_string = ""
        # For every file in the list
        for file in files:
            # Add this HTML code for a button to the string
            html_string += f"""
            <form method=post enctype=multipart/form-data>
            <input type=submit value="{file}" name="{file}">
            </form>\n"""
            # When finished return the string
        return html_string
    # Else return a message saying that there are no files
    else:
        return '<h1>There are no files upload, go to <a href="/upload">/upload</a> and upload some files.'
