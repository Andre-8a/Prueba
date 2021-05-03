from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/html", methods=["GET"])
def home():
	return render_template("Examen.html")

@app.route("/integrantes", methods=["GET"])
def integrantes():
	return "Nombre de los integrantes!" 


app.run()