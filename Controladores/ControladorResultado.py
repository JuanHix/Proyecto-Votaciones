from Modelos.Resultado import Resultado
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa
from Repositorios.ResultadoRepo import ResultadoRepo
from Repositorios.CandidatoRepo import CandidatoRepo
from Repositorios.MesaRepo import MesaRepo

class ControladorResultado():
    def __init__(self):
        self.resultadoRepo = ResultadoRepo()
        self.candidatoRepo = CandidatoRepo()
        self.mesaRepo = MesaRepo()
    def index(self):
        return self.resultadoRepo.findAll()
    
# Asignacion mesa-candidato a Resultado

    def create(self,infoResultado,id_candidato,id_mesa):
        nuevoResultado=Resultado(infoResultado)
        elCandidato=Candidato(self.candidatoRepo.findById(id_candidato))
        laMesa=Mesa(self.mesaRepo.findById(id_mesa))
        nuevoResultado.candidato=elCandidato
        nuevoResultado.mesa=laMesa
        return self.resultadoRepo.save(nuevoResultado)
    def show(self,id):
        elResultado=Resultado(self.resultadoRepo.findById(id))
        return elResultado.__dict__
 
# Modificacion de resultado (candidato y mesa)  

    def update(self,id,infoResultado,id_candidato,id_mesa):
        elResultado=Resultado(self.resultadoRepo.findById(id))
        elResultado.numero_mesa=infoResultado["numero_mesa"]
        elResultado.id_partido=infoResultado["id_partido"]
        elCandidato = Candidato(self.candidatoRepo.findById(id_candidato))
        laMesa = Mesa(self.mesaRepo.findById(id_mesa))
        elResultado.candidato = elCandidato
        elResultado.mesa = laMesa
        return self.resultadoRepo.save(elResultado)
    def delete(self, id):
        return self.resultadoRepo.delete(id)