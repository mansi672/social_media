from flask import Flask, render_template, request, redirect, url_for
import os
from scheduler import schedule  # Import the schedule_post function

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/schedule', methods=['POST'])
def schedule():
    caption = request.form['caption']
    schedule_time = request.form['scheduleTime']
    platforms = request.form.getlist('platforms')
    image = request.files['image']

    if image:
        image_path = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(image_path)
    
    # Call the schedule_post function from scheduler.py
    schedule_post(caption, schedule_time, platforms, image_path)

    return redirect(url_for('index'))

if __name__ == '_main_':
    if not os.path.exists(app.config['UPLOAD_FOLDER']):
        os.makedirs(app.config['UPLOAD_FOLDER'])
    app.run(debug=True)