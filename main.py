
from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)
from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorPartido import ControladorPartido
miControladorMesa = ControladorMesa()
miControladorCandidato = ControladorCandidato()
miControladorPartido = ControladorPartido()

# Test servidor
def test():
    json = {}
    json["message"] = "Servidor en Ejecucion..."
    return jsonify(json)

# Endpoint Candidato
@app.route("/candidato", methods=['GET'])
def getCandidatos():
    json = miControladorCandidato.index()
    return jsonify(json)

@app.route("/candidato", methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)

@app.route("/candidato/<string:id>", methods=['GET'])
def getCandidato(id):
    json = miControladorCandidato.show(id)
    return jsonify(json)

@app.route("/candidato/<string:id>", methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json = miControladorCandidato.update(id, data)
    return jsonify(json)

@app.route("/candidato/<string:id>", methods=['DELETE'])
def eliminarCandidato(id):
    json = miControladorCandidato.delete(id)
    return jsonify(json)

# Endpoint Mesa

@app.route("/mesa",methods=['GET'])
def getMesas():
    json=miControladorMesa.index()
    return jsonify(json)

@app.route("/mesa/<string:id>",methods=['GET'])
def getMesa(id):
    json=miControladorMesa.show(id)
    return jsonify(json)

@app.route("/mesa",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)

@app.route("/mesa/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json=miControladorMesa.update(id,data)
    return jsonify(json)

@app.route("/mesa/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)

# Endpoint Partido

@app.route("/partido",methods=['GET'])
def getPartidos():
    json=miControladorPartido.index()
    return jsonify(json)

@app.route("/partido/<string:id>",methods=['GET'])
def getPartido(id):
    json=miControladorPartido.show(id)
    return jsonify(json)

@app.route("/partido",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)

@app.route("/partido/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)

@app.route("/partido/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)

# Mensaje Servidor
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data


if __name__ == '__main__':
    dataConfig = loadFileConfig()
    print("Server running : "+"http://"+dataConfig["url-backend"]+":" + str(dataConfig["port"]))
    serve(app, host=dataConfig["url-backend"], port=dataConfig["port"])


'''
import pymongo
import certifi

ca = certifi.where()
client = pymongo.MongoClient("mongodb+srv://Admin:admin987@cluster0.kajv3bt.mongodb.net/?retryWrites=true&w=majority",tlsCAFile=ca)

db = client.test
print(db)

baseDatos = client["db-resultados-votaciones"]
print(baseDatos.list_collection_names())


'''