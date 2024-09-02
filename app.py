
from flask import Flask, render_template
from get_data import grab_data, finalize_data

app = Flask(__name__)

@app.route('/')
def index():
#    stuff =
    return render_template('index.html', data = 'stuff')
