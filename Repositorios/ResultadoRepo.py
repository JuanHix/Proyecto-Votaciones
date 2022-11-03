from Repositorios.InterfaceRepositorio import InterfaceRepositorio
from Modelos.Resultado import Resultado
from bson import ObjectId


class ResultadoRepo(InterfaceRepositorio[Resultado]):

    # Muestra las votaciones por mesa
    def getListadoCandidatosInscritosMesa(self, id_mesa):
        theQuery = {"mesa.$id": ObjectId(id_mesa)}
        return self.query(theQuery)

    # Muestra las votaciones por candidato
    def getListadoMesasCandidatoInscrito(self, id_candidato):
        theQuery1 = {"candidato.$id": ObjectId(id_candidato)}
        return self.query(theQuery1)

    # Numero mayor de una cédula
    def getNumeroCedulaMayorCandidato(self):
        query1 = {
            "$group":{
                "_id": "$candidato",
                "max": {
                    "$max": "$cedula"
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }

        pipeline = [query1]
        return self.queryAggregation(pipeline)

    # Suma de votos mesa
    def getSumaVotosPorMesa(self):
        query1 = {
            "$group": {
                "_id": "$mesa",
                "Total votos en todas las mesas": {
                    "$sum": 1
                },
                "doc": {
                    "$first": "$$ROOT"
                }
            }
        }

        pipeline = [query1]
        return self.queryAggregation(pipeline)
    