from flask import Flask, send_file, request
from werkzeug.utils import secure_filename
import os
app = Flask(__name__, static_url_path='/static')

uploads_dir = os.path.join(app.instance_path, 'uploads')


@app.route('/transfer')
def download_wav():
    # upload a .wav file (at endpoint for result)
    # We'll just run the transfer here?
    # Or we could do it once we get both audio files

    transferred_audio = 'static/audio_test.wav'
    return send_file(transferred_audio)


# recieve .wav file at content endpoint


# receive .wav file at style endpoint
@app.route('/upload_style', methods=['GET', 'POST', 'PUT'])
def upload_style():
    if request.method == 'POST' or request.method == 'PUT':
        style_file = request.files['file']
        file_path = uploads_dir + '/' + secure_filename('style.wav')
        print(f'saving to: {file_path}')
        style_file.save(file_path)
        # note: If the file already exists, it just overwrites it
        return "success"


@app.route('/upload_content', methods=['GET', 'POST', 'PUT'])
def upload_content():
    if request.method == 'POST' or request.method == 'PUT':
        content_file = request.files['file']
        file_path = uploads_dir + '/' + secure_filename('content.wav')
        print(f'saving to: {file_path}')
        content_file.save(file_path)
        # note: If the file already exists, it just overwrites it
        return "success"
