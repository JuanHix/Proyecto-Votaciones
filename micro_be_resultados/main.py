from flask import Flask, request, Response
from flask import jsonify
from flask_cors import CORS


from Controladores.ControladorCandidato import ControladorCandidato
from Controladores.ControladorMesa import ControladorMesa
from Controladores.ControladorPartido import ControladorPartido
from Controladores.ControladorResultado import ControladorResultado

app = Flask(__name__)
cors = CORS(app)

# -- Variables --  
miControladorMesa = ControladorMesa()
miControladorCandidato = ControladorCandidato()
miControladorPartido = ControladorPartido()
miControladorResultado = ControladorResultado()

#   Prueba      
@app.route("/", methods=["GET"])
def test():
    json = {}
    json["message"] = "Servidor en Ejecucion..."
    return jsonify(json)

# -- EndPoints Candidato --       

# Obtener o listar todos los candidatos.
@app.route("/candidato", methods=['GET'])
def getCandidatos():
    json = miControladorCandidato.index()
    return jsonify(json)

# Crear un candidato.
@app.route("/candidato", methods=['POST'])
def crearCandidato():
    data = request.get_json()
    json = miControladorCandidato.create(data)
    return jsonify(json)

# Obtener un candidato en especifico.
@app.route("/candidato/<string:id>", methods=['GET'])
def getCandidato(id):
    json = miControladorCandidato.show(id)
    return jsonify(json)

# Actualizar un candidato en especifico
@app.route("/candidato/<string:id>", methods=['PUT'])
def modificarCandidato(id):
    data = request.get_json()
    json = miControladorCandidato.update(id, data)
    return jsonify(json)

# Borrar un candidato en especifico
@app.route("/candidato/<string:id>", methods=['DELETE'])
def eliminarCandidato(id):
    json = miControladorCandidato.delete(id)
    return jsonify(json)

# Asignar un partido politico a un candidato. 
@app.route("/candidato/<string:id_candidato>/partido/<string:id_partido>", methods=["PUT"])
def asignarPartidoCandidato(id_candidato, id_partido):
    json = miControladorCandidato.asignarCandidato(id_candidato, id_partido)
    return jsonify(json)


# -- EndPoint Mesa --     


# Obtener o listar todas las mesas.
@app.route("/mesa",methods=['GET'])
def getMesas():
    json=miControladorMesa.index()
    return jsonify(json)

# Obtener o listar una mesas en especifico.
@app.route("/mesa/<string:id>",methods=['GET'])
def getMesa(id):
    json=miControladorMesa.show(id)
    return jsonify(json)

# Crear un mesa de votacion.
@app.route("/mesa",methods=['POST'])
def crearMesa():
    data = request.get_json()
    json=miControladorMesa.create(data)
    return jsonify(json)

# Obtener o listar una mesa de votacion en especifico.
@app.route("/mesa/<string:id>",methods=['PUT'])
def modificarMesa(id):
    data = request.get_json()
    json=miControladorMesa.update(id, data)
    return jsonify(json)

# Borrar una mesa de votacion en especifico.
@app.route("/mesa/<string:id>",methods=['DELETE'])
def eliminarMesa(id):
    json=miControladorMesa.delete(id)
    return jsonify(json)


# -- EndPoints Partido --         


# Obtener o listar todas los patidos politicos.
@app.route("/partido",methods=['GET'])
def getPartidos():
    json=miControladorPartido.index()
    return jsonify(json)

# Obtener o listar un partido politico en especifico.
@app.route("/partido/<string:id>",methods=['GET'])
def getPartido(id):
    json=miControladorPartido.show(id)
    return jsonify(json)

# Crear un partido politico
@app.route("/partido",methods=['POST'])
def crearPartido():
    data = request.get_json()
    json=miControladorPartido.create(data)
    return jsonify(json)

# Actualizar un partido Politico
@app.route("/partido/<string:id>",methods=['PUT'])
def modificarPartido(id):
    data = request.get_json()
    json=miControladorPartido.update(id,data)
    return jsonify(json)

# Eliminar un partido politico
@app.route("/partido/<string:id>",methods=['DELETE'])
def eliminarPartido(id):
    json=miControladorPartido.delete(id)
    return jsonify(json)

# -- EndPoint Resultado --       

# Obtener o listar todos los resultados.
@app.route("/resultado",methods=['GET'])
def getResultados():
    json=miControladorResultado.index()
    return jsonify(json)

# Obtener o listar un resultado en especifico. 
@app.route("/resultado/<string:id>",methods=['GET'])
def getResultado(id):
    json=miControladorResultado.show(id)
    return jsonify(json)

# Crear un resultado de votacion. 
@app.route("/resultado/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods =["POST"])
def crearResultado(id_mesa, id_candidato):
    data = request.get_json()
    json = miControladorResultado.create(data, id_mesa, id_candidato)
    return jsonify(json)

# Actualiazr un resultado en especifico. 
@app.route("/resultado/<string:id_resultado>/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods=["PUT"])
def modificarResultado(id_resultado, id_mesa, id_candidato):
    data={}
    json = miControladorResultado.update(id_resultado, data, id_mesa, id_candidato)
    return jsonify(json)

# Eliminar un resultadio en especifico. 
@app.route("/resultado/<string:id_resultado>",methods=['DELETE'])
def eliminarResultado(id_resultado):
    json=miControladorResultado.delete(id_resultado)
    return jsonify(json)

# Buscar los candidatos votados en una mesa
@app.route("/resultados/mesa/<string:id_mesa>", methods=["GET"])
def inscritosMesa(id_mesa):
    json = miControladorResultado.getListarCandidatosMesa(id_mesa)
    return jsonify(json)

# Buscar el candidato en las mesas
@app.route("/resultados/mesas/<string:id_candidato>", methods=["GET"])
def inscritoEnMesas(id_candidato):
    json = miControladorResultado.getListarMesasDeInscritoCandidato(id_candidato)
    return jsonify(json)

# Buscar cédula
@app.route("/resultados/documento", methods=["GET"])
def getMaxDocument():
    json = miControladorResultado.getMayorCedula()
    return jsonify(json)

# Total de votaciones por mesa.
@app.route("/resultados/votos", methods=["GET"])
def getSumaVotos():
    json = miControladorResultado.getSumaVotosMesa()
    return jsonify(json)


if __name__ == '__main__':
    app.run(debug=False, port=9000)
    
    