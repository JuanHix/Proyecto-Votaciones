
from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
import json
from waitress import serve

app = Flask(__name__)
cors = CORS(app)
from Controladores.ControladorCandidato import ControladorCandidato
miControladorCandidato = ControladorCandidato()

##############################################################################################################
@app.route("/", methods=['GET'])  # endpoint
def test():
    json = {}
    json["message"] = "Servidor en Ejecucion..."
    return jsonify(json)
#############################################################################################################

@app.route("/candidato", methods=['GET'])
def getCandidato():
    json = miControladorCandidato.index()
    return jsonify(json)

@app.route("/candidato", methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)

@app.route("/candidato/<string:id>", methods=['GET'])
def getandidato(id):
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


############################################################################################################################
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