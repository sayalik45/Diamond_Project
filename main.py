
import flask
from flask import Flask,render_template,request
import numpy as np

from utils import diamond_prediction

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/get_data',methods = ['POST','GET'])
def get_data():
    data = request.form
    class_obj = diamond_prediction(data)
    result = class_obj.price_prediction()
    return render_template('index.html',prediction = result)


    

if __name__ == "__main__":
    app.run(host = '0.0.0.0')