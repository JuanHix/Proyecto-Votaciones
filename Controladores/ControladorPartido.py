from Repositorios.PartidoRepo import PartidoRepo
from Modelos.Partido import Partido

class ControladorPartido():
    
    # Constructor
    def __init__(self):
        self.partidoRepo = PartidoRepo()
        
    # Devuelve todos los documentos
    def index(self):
        return self.partidoRepo.findAll()

    # Crea documentos
    def create(self, infoPartido):
        nuevoPartido = Partido(infoPartido)
        return self.partidoRepo.save(nuevoPartido)
    
    # Muestra un documento
    def show(self, id):
        elPartido = Partido(self.partidoRepo.findById(id))
        return elPartido.__dict__
    
    # Actualiza un documento
    def update(self, id, infoPartido):
        partidoActual = Partido(self.partidoRepo.findById(id))
        partidoActual.nombre = infoPartido["nombre"]
        partidoActual.lema = infoPartido["lema"]
        return self.partidoRepo.save(partidoActual)
    
    # Borra un documento
    def delete(self, id):
        return self.partidoRepo.delete(id)
    
    
        