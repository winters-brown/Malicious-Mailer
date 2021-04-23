"""
Author: Joshua Winters-Brown
flaskExample.py (c) 2021
Description: description
Created:  2021-04-23T17:20:13.807Z
"""
import os
from flask import Flask
from flask import request
from flask import render_template

# TODO: Read through a configuration file and parse these out lol
FLASK_ENV = 'development'  # develpment or production
UPLOAD_FOLDER = target = os.path.join(str(os.getcwd()), 'uploaded')
SECRET_KEY = str(os.urandom(16))
UPLOAD_EXTENSIONS = ['.html', '.md']

# TODO: Make better LOL
try:
    os.makedirs(UPLOAD_FOLDER)
except FileExistsError:
    pass

# TODO: Read through a configuration file
app = Flask(__name__, static_url_path='/static')
app.config['FLASK_ENV '] = FLASK_ENV
app.config['SECRET_KEY'] = SECRET_KEY
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['UPLOAD_EXTENSIONS'] = UPLOAD_EXTENSIONS


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/email', methods=['POST'])
def email():
    # TODO: Better code lol
    content = request.form
    for uploadedFile in request.files.getlist('file'):
        tempFileName = str(uploadedFile.filename).strip()
        tempFileName = tempFileName.replace(" ", "")
        uploadedFile.save(os.path.join(UPLOAD_FOLDER, tempFileName))

    # TODO: now run the emailer script with the location of the new file
    return "Thanks!"


if __name__ == "__main__":
    app.run()
