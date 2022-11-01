from Repositorios.MesaRepo import MesaRepo
from Modelos.Mesa import Mesa

class ControladorMesa():
    
    #Constructor.  
    def __init__(self):
        self.mesaRepo = MesaRepo()

    # Regresa todos los documentos.
    def index(self):
        return self.mesaRepo.findAll()

    # Crea documentos
    def create(self, infoMesa):
        nuevoMesa = Mesa(infoMesa)
        return self.mesaRepo.save(nuevoMesa)
    
    # Muestra un documento
    def show(self, id):
        laMesa = Mesa(self.mesaRepo.findById(id))
        return laMesa.__dict__

    # Actualiza un documento
    def update(self, id, infoMesa):
        mesaActual = Mesa(self.mesaRepo.findById(id))
        mesaActual.numero = infoMesa["numero"]
        mesaActual.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        return self.mesaRepo.save(mesaActual)

    # Borra un documento
    def delete(self, id):
        return self.mesaRepo.delete(id)
    
    