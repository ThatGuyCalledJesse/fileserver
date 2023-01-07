from flask import Flask, request, redirect, url_for, send_file, flash
from werkzeug.utils import secure_filename
from clear_files import clear_files
from buttons import create_buttons
import os


# Function declarations
def send_from_directory(directory: str, filename: str):
    file = send_file(os.path.join(directory, filename), as_attachment=True)
    os.system(f'rm uploads/{filename}')
    return file


app = Flask(__name__)
app.config['SECRET_KEY'] = 'admin'
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/')
def home():
    return """
<h1>Homepage</h1>
<p>This is the homepage, go to /upload or /download</p>    
"""


@app.route('/download/<filename>')
def download_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


@app.route('/download')
def download_page():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return create_buttons(files)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.form.get('clear') == 'Clear Files':
        clear_files()
        return '<h1>Files Cleared</h1>'
    else:
        if request.method == 'POST':
            # check if the post request has the file part
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            # if user does not select file, browser also
            # submit an empty part without filename
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect(url_for('upload_file', filename=filename))
        return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    <h1>Clear Files</h1>
    <form method=post enctype=multipart/form-data>
      <input type=submit value='Clear Files' name='clear'>
    </form>
    <h1>The site is supposed to crash after clear, might fix it one day</h1>
    '''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
