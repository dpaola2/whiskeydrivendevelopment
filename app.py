#! /usr/bin/env python

import os
from flask import Flask, flash, render_template
from markdown import markdown

app = Flask(__name__)

PORT = int(os.environ.get("PORT", '5000'))

@app.route('/')
def index():
    content = markdown(open("README.md").read())
    return render_template('index.html', content=content)

app.debug = os.environ.get('DEBUG', False)
app.run(host='0.0.0.0', port=PORT)
