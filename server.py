from flask import Flask, request, redirect, url_for, send_file, flash, render_template
from werkzeug.utils import secure_filename
from clear_files import clear_files
from buttons import create_buttons
import os


# Function declarations
# This function takes a directory and a file as input and returns the file as an attachment for HTML
def send_from_directory(directory: str, filename: str):
    file = send_file(os.path.join(directory, filename), as_attachment=True)
    os.system(f'rm uploads/{filename}')
    return file


# Create an 'app' variable and set the static_folder to 'static'
app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = 'admin'
# creating uploads folder if it doesn't exist
if not os.path.exists('uploads'):
    os.mkdir(os.path.join(os.getcwd(), 'uploads'))
app.config['UPLOAD_FOLDER'] = 'uploads'


# This route and function creates the index.html template
@app.route('/')
def home():
    return render_template("index.html")


# This route and function creates the download page and calls the create_buttons function for the HTML code
@app.route('/download', methods=['GET', 'POST'])
def download_page():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    if request.method == 'POST':
        for file in files:
            if request.form.get(f'{file}') == f'{file}':
                return send_from_directory(app.config['UPLOAD_FOLDER'], f'{file}')
    return create_buttons(files)


# This route and function creates the upload page and calls the clear file function
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    # If the post request is 'clear'
    if request.form.get('clear') == 'Clear Files':
        # Then call clear_files and remove all cleared files
        clear_files()
    # I actually have no idea what this code does, it was made by ChatGPT, so don't remove to prevent bugs
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


# Run the app
if __name__ == '__main__':
    # On the Wi-Fi network and port 8000
    app.run(host='0.0.0.0', port=8000)
