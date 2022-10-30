from Repositorios.CandidatoRepo import CandidatoRepo
from Modelos.Candidato import Candidato


class ControladorCandidato():
    def __init__(self):
        self.candidatoRepo = CandidatoRepo()

    def index(self):
        return self.candidatoRepo.findAll()

    def create(self, infoCandidato):
        nuevoCandidato = Candidato(infoCandidato)
        return self.candidatoRepo.save(nuevoCandidato)

    def show(self, id):
        elCandidato = Candidato(self.candidatoRepo.findById(id))
        return elCandidato.__dict__

    def update(self, id, infoCandidato):
        candidatoActual = Candidato(self.candidatoRepo.findById(id))
        candidatoActual.cedula = infoCandidato["cedula"]
        candidatoActual.numero_resolucion = infoCandidato["numero_resolucion"]
        candidatoActual.nombre = infoCandidato["nombre"]
        candidatoActual.apellido = infoCandidato["apellido"]
        return self.candidatoRepo.save(candidatoActual)

    def delete(self, id):
        return self.candidatoRepo.delete(id)
