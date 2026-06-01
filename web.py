from flask import Flask, render_template, request

web = Flask(__name__)

@web.route("/")
def inicio():
    return render_template("index.html")

@web.route("/quiz", methods=["POST"])
def quiz():

    puntos = 0

    if request.form["pregunta1"] == "b":
        puntos += 1

    if request.form["pregunta2"] == "a":
        puntos += 1

    if request.form["pregunta3"] == "a":
        puntos += 1

    return f"Obtuviste {puntos} de 3 puntos."

web.run(debug=True)
