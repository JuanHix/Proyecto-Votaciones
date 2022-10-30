from Repositorios.MesaRepo import MesaRepo
from Modelos.Mesa import Mesa

class ControladorMesa():
    def __init__(self):
        self.mesaRepo = MesaRepo()

    def index(self):
        return self.mesaRepo.findAll()

    def create(self, infoMesa):
        nuevoMesa = Mesa(infoMesa)
        return self.mesaRepo.save(nuevoMesa)

    def show(self, id):
        laMesa = Mesa(self.mesaRepo.findById(id))
        return laMesa.__dict__

    def update(self, id, infoMesa):
        mesaActual = Mesa(self.mesaRepo.findById(id))
        mesaActual.numero_mesa = infoMesa["numero_mesa"]
        mesaActual.cantidad_inscritos = infoMesa["cantidad_inscritos"]
        
        return self.mesaRepo.save(mesaActual)

    def delete(self, id):
        return self.mesaRepo.delete(id)
    
    