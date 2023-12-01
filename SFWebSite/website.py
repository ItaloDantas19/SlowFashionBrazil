import numpy as np
from  flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open('SFWebSite\SFmodelo.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.htm')