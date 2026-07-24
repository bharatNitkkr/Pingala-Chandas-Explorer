from flask import Flask, render_template, request

from algorithms import (
    prastara,
    nasta,
    uddista,
    sankhya,
    adhvayoga,
    meru_prastara,
    matra_chandas,
    matra_meru,
    permutation_algorithm,
    gana_decoder,
    pattern_analyzer,
    chandas_identifier,
)
from sutra_data import SUTRA_DETAILS


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

    return render_template(
        "prastara.html",
        result=result,
        sutra=SUTRA_DETAILS["prastara"],
    )


@app.route("/nasta", methods=["GET", "POST"])
def nasta_page():
    result = None
    error = None

    if request.method == "POST":
        n = int(request.form["n"])
        index = int(request.form["index"])
        result = nasta(n, index)

        if result is None:
            error = (
                f"Invalid rank. For n = {n}, "
                f"rank must be between 1 and {2 ** n}."
            )

    return render_template(
        "nasta.html",
        result=result,
        error=error,
        sutra=SUTRA_DETAILS["nasta"],
    )


@app.route("/uddista", methods=["GET", "POST"])
def uddista_page():
    result = None
    error = None

    if request.method == "POST":
        pattern = request.form["pattern"].upper().strip()
        result = uddista(pattern)

        if result is None:
            error = "Invalid pattern. Please use L/G or 0/1 only."

    return render_template(
        "uddista.html",
        result=result,
        error=error,
        sutra=SUTRA_DETAILS["uddista"],
    )


@app.route("/sankhya", methods=["GET", "POST"])
def sankhya_page():
    result = None

    if request.method == "POST":
        n = int(request.form["n"])
        result = sankhya(n)

    return render_template(
        "sankhya.html",
        result=result,
        sutra=SUTRA_DETAILS["sankhya"],
    )


@app.route("/adhvayoga", methods=["GET", "POST"])
def adhvayoga_page():
    result = None

    if request.method == "POST":
        n = int(request.form["n"])
        result = adhvayoga(n)

    return render_template(
        "adhvayoga.html",
        result=result,
        sutra=SUTRA_DETAILS["adhvayoga"],
    )


@app.route("/meru", methods=["GET", "POST"])
def meru_page():
    result = None

    if request.method == "POST":
        n = int(request.form["n"])
        result = meru_prastara(n)

    return render_template(
        "meru.html",
        result=result,
        sutra=SUTRA_DETAILS["meru"],
    )


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


@app.route("/matra-meru", methods=["GET", "POST"])
def matra_meru_page():
    result = None

    if request.method == "POST":
        m = int(request.form["m"])
        result = matra_meru(m)

    return render_template("matra_meru.html", result=result)


@app.route("/permutation", methods=["GET", "POST"])
def permutation_page():
    result = None

    if request.method == "POST":
        items_text = request.form["items"]
        items = [item.strip() for item in items_text.split(",")]
        result = permutation_algorithm(items)

    return render_template("permutation.html", result=result)


@app.route("/other-algorithms")
def other_algorithms():
    return render_template("other_algorithms.html")


@app.route("/gana-decoder", methods=["GET", "POST"])
def gana_decoder_page():
    result = None
    error = None

    if request.method == "POST":
        pattern = request.form["pattern"]
        result = gana_decoder(pattern)

        if result is None:
            error = "Invalid input. Please use only L/G or 1/0."

    return render_template(
        "gana_decoder.html",
        result=result,
        error=error,
    )


@app.route("/pattern-analyzer", methods=["GET", "POST"])
def pattern_analyzer_page():
    result = None
    error = None

    if request.method == "POST":
        pattern = request.form["pattern"]
        result = pattern_analyzer(pattern)

        if result is None:
            error = "Invalid input. Please use only L/G or 1/0."

    return render_template(
        "pattern_analyzer.html",
        result=result,
        error=error,
    )


@app.route("/chandas-identifier", methods=["GET", "POST"])
def chandas_identifier_page():
    result = None
    error = None

    if request.method == "POST":
        pattern = request.form["pattern"]
        result = chandas_identifier(pattern)

        if result is None:
            error = "Invalid input. Please use only L/G or 1/0."

    return render_template(
        "chandas_identifier.html",
        result=result,
        error=error,
    )


if __name__ == "__main__":
    app.run(debug=True)
