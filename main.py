from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('length.html')

@app.route("/length")
def length():
    return render_template('length.html')

@app.route("/weight")
def weight():
    return render_template("weight.html")

@app.route("/temperature")
def temperature():
    return render_template("temperature.html")

@app.route("/convert")
def convert():
    return render_template("result.html")

if __name__ == "__main__":
    app.run(debug=True)