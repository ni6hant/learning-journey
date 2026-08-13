from flask import Flask, render_template, request
from datetime import datetime

app = Flask(__name__)


now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")

@app.route("/")
def index():
    return render_template('index.html',word="Poppy",dateTime=dt_string)