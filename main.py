from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    render_template('form.html')