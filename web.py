from flask import Flask, render_template

web = Flask(__name__)

@web.route("/")
def inicio():
    return render_template("index.html")

web.run(debug=True)
