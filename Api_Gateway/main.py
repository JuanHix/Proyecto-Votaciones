from flask import Flask, jsonify, request
from flask_cors import CORS
from waitress import serve  # Conexion a el servidor
import datetime  # maneja tiempos del token
import requests
import re   # limpia las url
import json # Conviete de diccionario a Json y viceversa

app = Flask(__name__)
cors = CORS(app)      # Se pasa el Cors a la aplicacion para no generar conflicto con Firewall


#  Librerias JWT Seguridad        

from flask_jwt_extended import create_access_token, verify_jwt_in_request # Crea token de acceso
from flask_jwt_extended import get_jwt_identity  # Identidad del Token
from flask_jwt_extended import jwt_required    
from flask_jwt_extended import JWTManager # utiliza la aplicacion para darle lo atributos de seguridad


# Creacion Token Seguridad  credencial acceso        

app.config["JWT_SECRET_KEY"] = 'Admin987' 
jwt = JWTManager(app) # Pasamos la configuracion de JWT a la app

@app.route("/login", methods=['POST']) # Ruta para creacion del token
def create_token():
    data = request.get_json()  # Respueta de la peticion 
    headers = {"Content-Type": "application/json; charset=utf-8"} # encabezados de la peticion
    url = dataConfig["url-backend-security"]+"/usuarios/validar" # Valida en el backend de seguridad si el usuario esta registrado.
    response = requests.post(url, json= data, headers=headers) # se lleva acaba la peticion
    if response.status_code == 200:   # respuesta satisfactoria usuario existe en la base de datos
        user = response.json() # respuesta con datos de usuario en json
        expires = datetime.timedelta(seconds=60*60*24) # tiempo de expiracion del token
        access_token = create_access_token(identity=user, # creacion del token
            expires_delta=expires)
        return jsonify({"token": access_token, # retorna respuesta del token 
            "user_id": user["_id"]})
    else:
        return jsonify({
            "Message": "correo o contraseña invalidos. "
        }), 401


# MIDDLEWARE            
# Nos permite pasarnos por los Endpoints y hacer consultas que haya autenticado por token.

# Limpiar la url y buscar id cambiar por ?
def limpiarURL(url):
    partes = request.path.split("/")  # Separamos la url por partes con slipt
    for laParte in partes:     
        if re.search('\\d', laParte):  # Buscamos en la url y el object id lo remplazamos por ?
            url = url.replace(laParte, "?")
    return url

# Si el Id tiene permiso para aceder a la url con el metodo.
def validarPermiso(endPoint, metodo, idRol):
    url = dataConfig["url-backend-security"]+ "/permisos-roles/validar-permiso/rol/"+str(idRol) # Armamos la url 
    tienePermiso= False # no tiene permiso hasta que no se valide
    headers = {"Content-Type": "application/json; charset=utf-8"}
    body = {
        "url": endPoint,
        "metodo": metodo
    }
    response = requests.get(url, json=body, headers=headers) # respuesta
    try: 
        data = response.json()
        if("_id" in data):
            tienePermiso = True  # le damos permiso
    except:
        pass
    return tienePermiso

# Permite encaminar las peticiones con la seguridad
@app.before_request
def before_request_callback():         # validar 
    endPoint = limpiarURL(request.path)
    excludedRoutes = ["/login"] # ignoramos la ruta login 
    if excludedRoutes.__contains__(request.path):
        print("ruta excluida ", request.path)
        pass
    elif verify_jwt_in_request():    # cuando la ruta no esta excluida
        usuario = get_jwt_identity()
        if usuario["rol"] is not None: # si el rol esta definido o no
            tienePermiso =  validarPermiso(endPoint,
                request.method, usuario["rol"]["_id"]) # si tiene permiso pasamos los datos(endPoint, metodo, usuario, rol,id)
            if not tienePermiso:
                return jsonify({          # si no tiene permiso retorna mensaje
                    "message ": "usted no tiene permisos"
                }), 401
        else:
            return jsonify({
                    "message ": "Verifique sus credenciales no corresponden los permisos"
                }), 401


# Metodos con ruta   

@app.route("/mesa", methods=["GET"]) # Ruta con el metodo
def getMesas():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+'/mesa'
    response = requests.get(url, headers=headers)
    Json = response.json() 
    return jsonify(Json) # llega en diccionario lo cambiamos a Json

@app.route("/mesa", methods=["POST"])
def crearMesa():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+'/mesa'
    response = requests.post(url, headers=headers, json=data)
    Json = response.json()
    return jsonify(Json)

@app.route("/mesa/<string:id>", methods=["GET"])
def getMesa(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+'/mesa/'+id
    response = requests.get(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

@app.route("/mesa/<string:id>", methods=["PUT"])
def modificarMesa(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+'/mesa/'+id
    response = requests.put(url, headers=headers, json=data)
    Json = response.json()
    return jsonify(Json)

@app.route("/mesa/<string:id>", methods=["DELETE"])
def deleteMesa(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+'/mesa/'+id
    response = requests.delete(url, headers=headers)
    Json = response.json()
    return jsonify(Json)


# Metodo con ruta Partidos  

@app.route("/partido", methods=["GET"])
def getPartidos():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+'/partido'
    response = requests.get(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

@app.route("/partido", methods=["POST"])
def crearPartido():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+'/partido'
    response = requests.post(url, headers=headers, json=data)
    Json = response.json()
    return jsonify(Json)

@app.route("/partido/<string:id>", methods=["GET"])
def getPartido(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+'/partido/'+id
    response = requests.get(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

@app.route("/partido/<string:id>", methods=["PUT"])
def modificarPartido(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+'/partido/'+id
    response = requests.put(url, headers=headers, json=data)
    Json = response.json()
    return jsonify(Json)

@app.route("/partido/<string:id>", methods=["DELETE"])
def deletePartido(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+'/partido/'+id
    response = requests.delete(url, headers=headers)
    Json = response.json()
    return jsonify(Json)


# metodo con ruta candidado

@app.route("/candidato", methods=["GET"])
def getCandidatos():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+'/candidato'
    response = requests.get(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

@app.route("/candidato", methods=["POST"])
def crearCandidato():
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+'/candidato'
    response = requests.post(url, headers=headers, json=data)
    Json = response.json()
    return jsonify(Json) 

@app.route("/candidato/<string:id>", methods=["GET"])
def getCandidato(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+'/candidato/'+id
    response = requests.get(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

@app.route("/candidato/<string:id>", methods=["PUT"])
def modificarCandidato(id):
    data = request.get_json()
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+'/candidato/'+id
    response = requests.put(url, headers=headers, json=data)
    Json = response.json()
    return jsonify(Json)

@app.route("/candidato/<string:id>", methods=["DELETE"])
def deleteCandidato(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+'/candidato/'+id
    response = requests.delete(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

@app.route("/candidato/<string:id_candidato>/partido/<string:id_partido>", methods=["PUT"])
def asignarCandidato(id_candidato, id_partido):
    data = {
        "candidato":{},
        "partido": {}
    }
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+"/candidato/"+id_candidato+"/partido/"+ id_partido
    response = requests.put(url, headers=headers, json= data)
    Json = response.json()
    return jsonify(Json)



# metodo con ruta Resultados  

@app.route("/resultado", methods=["GET"])
def getResultados():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+'/resultado'
    response = requests.get(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

@app.route("/resultado/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods =["POST"])
def crearResultado(id_mesa, id_candidato):
    data = {}
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+"/resultado/mesa/"+id_mesa+"/candidato/"+id_candidato
    response = requests.post(url, headers=headers, json=data)
    Json = response.json()
    return jsonify(Json)


@app.route("/resultado/<string:id>", methods=["GET"])
def getResultado(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+'/resultado/'+id
    response = requests.get(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

@app.route("/resultado/<string:id_resultado>/mesa/<string:id_mesa>/candidato/<string:id_candidato>", methods=["PUT"])
def modificarResultado(id_resultado, id_mesa, id_candidato):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+"/resultado/"+id_resultado+"/mesa/"+id_mesa+"/candidato/"+id_candidato
    response = requests.put(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

@app.route("/resultado/<string:id>", methods=["DELETE"])
def deleteResultado(id):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+'/resultado/'+id
    response = requests.delete(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

# Mirar los resultados de una mesa en particular

@app.route("/resultados/mesa/<string:id_mesa>", methods=["GET"])
def votosEnMesa(id_mesa):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+'/resultados/mesa/'+id_mesa
    response = requests.get(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

# Mirar los votos de un candidato en todas las mesas

@app.route("/resultados/mesas/<string:id_candidato>", methods=["GET"])
def votosCandidato(id_candidato):
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+'/resultados/mesas/'+id_candidato
    response = requests.get(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

# Conteo de los votos
@app.route("/resultado/maxdocument", methods=["GET"])
def getConteoVotos():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+'/resultado/maxdocument'
    response = requests.get(url, headers=headers)
    Json = response.json()
    return jsonify(Json)

# Total votos mesa
@app.route("/resultados/votos", methods=["GET"])
def getSumaVotos():
    headers = {"Content-Type": "application/json; charset=utf-8"}
    url = dataConfig["url-backend-results"]+'/resultados/votos'
    response = requests.get(url, headers=headers)
    Json = response.json()
    return jsonify(Json)


# test o prueba del servicio
@app.route("/", methods=['GET'])          # Endpoint prueba servidor 
def test():
    Json = {}
    Json["Message"]= "Server Running ..."
    return jsonify(Json)


#  Conexion      
def loadFileConfig():
    with open('config.json') as f:
        data = json.load(f)
    return data

if __name__ == "__main__":      
    dataConfig = loadFileConfig()       # Carga archivo
    print("Server url-backend running : http://"+
        dataConfig["url-backend"]+":"+
        dataConfig["port"])             # Imprime la url de conexion (pantalla)
    serve(app, host= dataConfig["url-backend"],  # Ejecucion con parametros
        port=dataConfig["port"])
    
    
    