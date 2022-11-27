from Repositorios.CandidatoRepo import CandidatoRepo
from Repositorios.PartidoRepo import PartidoRepo
from Modelos.Candidato import Candidato
from Modelos.Partido import Partido


class ControladorCandidato():
    
    # Constructores. 
    def __init__(self):
        self.candidatoRepo = CandidatoRepo()
        self.partidoRepo = PartidoRepo()
    
    # Devuelve todos los documentos.    
    def index(self):
        return self.candidatoRepo.findAll()

    # Crea documentos.
    def create(self, infoCandidato):
        nuevoCandidato = Candidato(infoCandidato)
        return self.candidatoRepo.save(nuevoCandidato)

    # Muestra un documento.
    def show(self, id):
        elCandidato = Candidato(self.candidatoRepo.findById(id))
        return elCandidato.__dict__
    
    # Actualiza un documento.
    def update(self, id, infoCandidato):
        candidatoActual = Candidato(self.candidatoRepo.findById(id))
        candidatoActual.cedula = infoCandidato["cedula"]
        candidatoActual.numero_resolucion = infoCandidato["numero_resolucion"]
        candidatoActual.nombre = infoCandidato["nombre"]
        candidatoActual.apellido = infoCandidato["apellido"]
        return self.candidatoRepo.save(candidatoActual)
    
    # Elimina un documento.
    def delete(self, id):
        return self.candidatoRepo.delete(id)
    
    # Relacion coleccion candidato-partido
    def asignarCandidato(self, id, id_partido):
        candidatoActual = Candidato(self.candidatoRepo.findById(id))
        partidoActual = Partido(self.partidoRepo.findById(id_partido))
        candidatoActual.partido = partidoActual
        return self.candidatoRepo.save(candidatoActual)
    

