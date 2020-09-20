from flask import Flask, render_template, request, redirect, url_for, abort #imports
from werkzeug.utils import secure_filename
import os

app = Flask(__name__) #create instance of server app
app.config['UPLOAD_PATH'] = '/home/pi/EduBox/Storage'

### URL to Upload One File ###

@app.route('/basic/') #default GET request url route

def index(): #display index.html for above url
    return render_template('index.html')


@app.route('/basic/', methods=['POST']) #POST request with same url route

def upload_file(): #store uploaded_file, save file, redirect back to index.html
    uploaded_file = request.files['file'] #'file' is name of input tag in html
    if uploaded_file.filename != '':
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], uploaded_file.filename))
    return redirect(url_for('index'))

### URL to Upload File with Responsive HTML Design and single function for all request methods###

@app.route('/responsive/', methods=['GET','POST']) #Requests for responsive url

def responsive(): #store uploaded_file, redirect back to index_responsive.html
    if request.method == 'POST':
        uploaded_file = request.files['file']
        if uploaded_file.filename != '':
            uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], uploaded_file.filename))
        return redirect(url_for('responsive'))
    return render_template('responsive_index.html')

### URL to Upload Multiple Image and Video Files Only ###

@app.route('/multiple/', methods=['GET','POST']) #Requests and url route

def multiple(): #store multiple files, redirect to accept_multiple.html
    if request.method == 'POST':
        for uploaded_file in request.files.getlist('images_and_videos'):
            if uploaded_file.filename != '':
                uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], uploaded_file.filename))
        return redirect(url_for('multiple'))
    return render_template('accept_multiple.html')

### URL to Securely Upload Image and Video Files - USE THIS ONE FOR UPLOAD###

@app.route('/', methods=['GET','POST']) #Requests and url route

def secure(): #store multiple files, redirect to multiple_css.html
    if request.method == 'POST':
        for uploaded_file in request.files.getlist('images_and_videos'):
            filename = secure_filename(uploaded_file.filename)
            if filename != '':
                file_ext = os.path.splitext(filename)
                if file_ext[1] == ".MOV":
                    filename = file_ext[0] + ".mp4"
                uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
        return redirect(url_for('secure'))
    return render_template('multiple_css.html') #same as multiple but w/ style

if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0',port=5000)
