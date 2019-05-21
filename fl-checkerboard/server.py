from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def regBoard():
    x = "8"
    y = "8"
    color1 = "red"
    color2 = "black"

    return render_template("index.html", x_columns=int(x), y_rows=int(y), color1=color1, color2=color2)


@app.route('/<x>')
def customBoard(x):
    y = "8"

    color1 = "red"
    color2 = "black"

    return render_template("index.html", x_columns=int(x), y_rows=int(y), color1=color1, color2=color2)


@app.route('/<x>/<y>')
def customSizeBoard(x, y):
    color1 = "red"
    color2 = "black"

    return render_template("index.html", x_columns=int(x), y_rows=int(y), color1=color1, color2=color2)


@app.route('/<x>/<y>/<color1>/<color2>')
def customColorBoard(x, y, color1, color2):
    # x = "8"
    # y = "8"
    # color1 = color1
    # color2 = color2

    return render_template("index.html", x_columns=int(x), y_rows=int(y), color1=color1, color2=color2)


if __name__ == "__main__":
    app.run(debug=True)
