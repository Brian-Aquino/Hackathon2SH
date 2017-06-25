"""
Routes and views for the flask application.
"""

from datetime import datetime
from flask import render_template
from FlaskWebProject1 import app
from flask import request
import requests
import json
import pdb
@app.route('/')
@app.route('/home')
def home():
    """Renders the home page."""
    return render_template(
        'index.html',
        title='Home Page',
        year=datetime.now().year,
    )
@app.route('/submit')

def submit():
    pdb.set_trace()
    a =  request.args.get("text")
    r = requests.post('http://sample-env-3.pixfhe7yjs.us-east-1.elasticbeanstalk.com/langAnalyze', data={"text":request.args.get("text")})
    return r.text