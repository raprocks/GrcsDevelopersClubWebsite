from flask import url_for, request, render_template
from . import app

@app.route('/')
def home():
    return render_template('index.html')
