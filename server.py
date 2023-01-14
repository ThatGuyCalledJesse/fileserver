from flask import Flask, request, redirect, url_for, send_file, flash, render_template
from werkzeug.utils import secure_filename
from clear_files import clear_files
from buttons import create_buttons
import os


# Function declarations
def send_from_directory(directory: str, filename: str):
    file = send_file(os.path.join(directory, filename), as_attachment=True)
    os.system(f'rm uploads/{filename}')
    return file


app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'admin'
# creating uploads folder if it doesn't exist
if not os.path.exists('uploads'):
    os.mkdir(os.path.join(os.getcwd(), 'uploads'))
app.config['UPLOAD_FOLDER'] = 'uploads'


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/download', methods=['GET', 'POST'])
def download_page():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    if request.method == 'POST':
        for file in files:
            if request.form.get(f'{file}') == f'{file}':
                return send_from_directory(app.config['UPLOAD_FOLDER'], f'{file}')
    return create_buttons(files)


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.form.get('clear') == 'Clear Files':
        clear_files()
        return '<h1>Files Cleared</h1>'
    else:
        if request.method == 'POST':
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
            if file:
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                return redirect(url_for('upload_file', filename=filename))
        return render_template('upload.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
