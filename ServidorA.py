from flask import Flask, render_template

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET"])
def home():
	return render_template("TrabajoA.html")

@app.route("/datos", methods=["GET"])
def tacos():
	return "Datos de la persona!" 


app.run()