from flask import Flask, request, render_template, redirect, url_for
from unit_converter import convert_measure, get_unit

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

@app.route("/convert", methods=['POST', 'GET'])
def convert():
    if request.method == 'POST':
        x = int(request.form['measure'])
        from_unit = request.form['convert_from']
        to_unit = request.form["convert_to"]
        convert_type = request.form['convert_type']
        context = {
        'input_measure': f"{x} {get_unit(from_unit)}",
        'output_measure':convert_measure(from_unit, to_unit, x, convert_type),
        }
        return render_template("result.html", **context)

if __name__ == "__main__":
    app.run(debug=True)