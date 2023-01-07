def create_buttons(files: list[str]):
    html_string = ""
    for file in files:
        html_string += f"""
<form method=post enctype=multipart/form-data>
<input type=submit value="{file}" name="{file}">
</form>\n
        """
    print(html_string)
    return html_string
<<<<<<< HEAD

=======
>>>>>>> origin/main
