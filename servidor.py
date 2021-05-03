# FLASK es un FRANEWORK APP WEB (BACKEND-SERVIDOR) PYTHON
# SERVIDOR
# RESPONDE
# HOGAR/PUNTO DE INICIO -> HOST
# VENTANILLA/PUERTA -> PORT(PUERTO)
# SERVIDOR -> DIRECCION = HOST:PORT
# IP ->  192.168.0.4 (HOST)
# LOCALHOST (127.0.0.1)
# PUERTO ESTANDAR: (HTTP/HTTPS) : 80 
# PUERTO DIFERENTE -> 3000, 5000, 6969, 8000, 8001, 8008

import flask


app = flask.Flask(__name__)
app.config["DEBUG"] = True

@app.route("/", methods=["GET"])
def home():
	return "<h1>Hola mundo me llamo Andre!</h1><br><button>Picame</button>"

@app.route("/tacos", methods=["GET"])
def tacos():
	return "Me gustan los tacos!" 

app.run()