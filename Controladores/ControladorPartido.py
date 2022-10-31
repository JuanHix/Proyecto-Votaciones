from Repositorios.PartidoRepo import PartidoRepo
from Repositorios.CandidatoRepo import CandidatoRepo
from Modelos.Partido import Partido
from Modelos.Candidato import Candidato

class ControladorPartido():
    def __init__(self):
        self.partidoRepo = PartidoRepo()
        self.candidatoRepo = CandidatoRepo()
        

    def index(self):
        return self.partidoRepo.findAll()

    def create(self, infoPartido):
        nuevoPartido = Partido(infoPartido)
        return self.partidoRepo.save(nuevoPartido)

    def show(self, id):
        elPartido = Partido(self.partidoRepo.findById(id))
        return elPartido.__dict__

    def update(self, id, infoPartido):
        partidoActual = Partido(self.partidoRepo.findById(id))
        partidoActual.nombre = infoPartido["nombre"]
        partidoActual.lema = infoPartido["lema"]
        
        return self.partidoRepo.save(partidoActual)

    def delete(self, id):
        return self.partidoRepo.delete(id)
    
    # Relacion Partido Candidato

    def asignarCandidato(self, id, id_candidato):
            partidoActual = Partido(self.partidoRepo.findById(id))
            candidatoActual = Candidato(self.candidatoRepo.findById(id_candidato))
            partidoActual.candidato = candidatoActual
            return self.partidoRepo.save(partidoActual)
        