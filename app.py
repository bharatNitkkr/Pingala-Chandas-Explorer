from flask import Flask, render_template, request
from algorithms import prastara, nasta, uddista, sankhya, adhvayoga, meru_prastara, matra_chandas

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/prastara", methods=["GET", "POST"])
def prastara_page():
    result = None

    if request.method == "POST":
        n = int(request.form["n"])
        result = prastara(n)

    return render_template("prastara.html", result=result)

@app.route("/nasta", methods=["GET", "POST"])
def nasta_page():
    result = None
    error = None

    if request.method == "POST":
        n = int(request.form["n"])
        index = int(request.form["index"])

        result = nasta(n, index)

        if result is None:
            error = f"Invalid rank. For n = {n}, rank must be between 1 and {2 ** n}."

    return render_template("nasta.html", result=result, error=error)

@app.route("/uddista", methods=["GET", "POST"])
def uddista_page():
    result = None
    error = None

    if request.method == "POST":
        pattern = request.form["pattern"].upper().strip()

        result = uddista(pattern)

        if result is None:
            error = "Invalid pattern. Please use L/G or 0/1 only."

    return render_template("uddista.html", result=result, error=error)

@app.route("/sankhya", methods=["GET", "POST"])
def sankhya_page():
    result = None

    if request.method == "POST":
        n = int(request.form["n"])
        result = sankhya(n)

    return render_template("sankhya.html", result=result)

@app.route("/adhvayoga", methods=["GET", "POST"])
def adhvayoga_page():
    result = None

    if request.method == "POST":
        n = int(request.form["n"])
        result = adhvayoga(n)

    return render_template("adhvayoga.html", result=result)

@app.route("/meru", methods=["GET", "POST"])
def meru_page():
    result = None

    if request.method == "POST":
        n = int(request.form["n"])
        result = meru_prastara(n)

    return render_template("meru.html", result=result)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/learn-chandas")
def learn_chandas():
    return render_template("learn_chandas.html")


@app.route("/lecture-interpretation")
def lecture_interpretation():
    return render_template("lecture_interpretation.html")


@app.route("/sutra-details")
def sutra_details():
    return render_template("sutra_details.html")


@app.route("/matra-chandas", methods=["GET", "POST"])
def matra_chandas_page():
    result = None

    if request.method == "POST":
        m = int(request.form["m"])
        result = matra_chandas(m)

    return render_template("matra_chandas.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)