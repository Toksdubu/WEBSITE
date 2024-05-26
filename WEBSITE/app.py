from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("HOMEPAGE.html")


@app.route("/Profile")
def profile():
    return render_template("PROFILE.html")


@app.route("/Upper", methods=["GET", "POST"])
def works():
    result = None
    if request.method == "POST":
        input_string = request.form.get("inputString", "")
        result = input_string.upper()
    return render_template("UPPER.html", result=result)


@app.route("/Circle", methods=["GET", "POST"])
def areaofc():
    result = None
    if request.method == "POST":
        input_radius = request.form.get("inputInteger", "")

        if input_radius and input_radius.isdigit():
            input_radius = int(input_radius)
            result = (input_radius**2 * 3.14)
        else:
            return "Invalid input. Please enter a valid integer for the radius."

    return render_template("CIRCLE.html", result=result)


@app.route("/Triangle", methods=["GET", "POST"])
def triangle():
    area = None

    if request.method == "POST":
        base = request.form.get("base")
        height = request.form.get("height")

        try:
            base = float(base)
            height = float(height)
            area = (base * height) / 2
        except ValueError:
            return "Invalid input. Please enter valid numbers for the base and height."

    return render_template("TRIANGLE.html", area=area)


@app.route("/Contact")
def contact():
    return render_template("CONTACTS.html")


if __name__ == "__main__":
    app.run(debug=True)
