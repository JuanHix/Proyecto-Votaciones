from Repositorios.PartidoRepo import PartidoRepo
from Modelos.Partido import Partido

class ControladorPartido():
    def __init__(self):
        self.partidoRepo = PartidoRepo()

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
    