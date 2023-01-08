def create_buttons(files: list[str]):
    if len(files) != 0:
        html_string = ""
        for file in files:
            html_string += f"""
        <form method=post enctype=multipart/form-data>
        <input type=submit value="{file}" name="{file}">
        </form>\n
                """
        return html_string
    else:
        return '<h1>There are no files upload, go to <a href="/upload">/upload</a> and upload some files.'
