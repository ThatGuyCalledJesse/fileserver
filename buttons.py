def create_buttons(files: list[str]):
    html_string = ""
    for file in files:
        html_string += f"""
        <form method="POST" enctype="multipart/form-data">
            <input type=submit value="{file}_value" name="{file}_name"
            </form>
        """
    return html_string
