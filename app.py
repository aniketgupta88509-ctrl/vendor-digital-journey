from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/payments")
def payments():
    return render_template("payments.html")


@app.route("/digital-tools")
def digital_tools():
    return render_template("digital-tools.html")


@app.route("/security-awareness")
def security_awareness():
    return render_template("security-awareness.html")

@app.route("/survey")
def survey():
    return render_template("survey.html")

@app.route("/official-sources")
def official_sources():
    return render_template("official-sources.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
    submitted = False

    if request.method == "POST":
        name = request.form.get("name")
        mobile = request.form.get("mobile")
        email = request.form.get("email")
        message = request.form.get("message")

        print("Name:", name)
        print("Mobile:", mobile)
        print("Email:", email)
        print("Message:", message)

        submitted = True

    return render_template("contact.html", submitted=submitted)

if __name__ == "__main__":
    app.run(debug=True)