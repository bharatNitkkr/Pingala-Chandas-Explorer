from flask import Flask, render_template, request
from algorithms import prastara, nasta, uddista, sankhya, adhvayoga, meru_prastara

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/prastara", methods=["GET", "POST"])
def prastara_page():
    result = None
    n = None

    if request.method == "POST":
        n = int(request.form["n"])
        result = prastara(n)

    return render_template("prastara.html", result=result, n=n)

@app.route("/nasta", methods=["GET", "POST"])
def nasta_page():
    result = None
    error = None

    if request.method == "POST":
        n = int(request.form["n"])
        index = int(request.form["index"])

        result = nasta(n, index)

        if result is None:
            error = f"Invalid index. For n = {n}, index must be between 1 and {2 ** n}."

    return render_template("nasta.html", result=result, error=error)

@app.route("/uddista", methods=["GET", "POST"])
def uddista_page():
    result = None
    error = None

    if request.method == "POST":
        pattern = request.form["pattern"].upper().strip()

        result = uddista(pattern)

        if result is None:
            error = "Invalid pattern. Please use only L for Laghu and G for Guru."

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
        rows = int(request.form["rows"])
        result = meru_prastara(rows)

    return render_template("meru.html", result=result)

@app.route("/about")
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)