from Repositorios.ResultadoRepo import ResultadoRepo
from Repositorios.CandidatoRepo import CandidatoRepo
from Repositorios.MesaRepo import MesaRepo

from Modelos.Resultado import Resultado
from Modelos.Candidato import Candidato
from Modelos.Mesa import Mesa


class ControladorResultado():
    
    # Constructores.
    def __init__(self):
        self.resultadoRepo = ResultadoRepo()
        self.candidatoRepo = CandidatoRepo()
        self.mesaRepo = MesaRepo()
    
    # Devuelve todos los documentos.   
    def index(self):
        return self.resultadoRepo.findAll()
    
    # Crea documentos.
    def create(self,infoResultado,id_mesa,id_candidato):
        nuevoResultado=Resultado(infoResultado)
        laMesa=Mesa(self.mesaRepo.findById(id_mesa))
        elCandidato=Candidato(self.candidatoRepo.findById(id_candidato))
        nuevoResultado.mesa=laMesa
        nuevoResultado.candidato=elCandidato
        return self.resultadoRepo.save(nuevoResultado)
    
    # Muestra un documento.
    def show(self,id):
        elResultado=Resultado(self.resultadoRepo.findById(id))
        return elResultado.__dict__
 
    # Actualiza un documento.
    def update(self,id,infoResultado,id_mesa,id_candidato):
        elResultado=Resultado(self.resultadoRepo.findById(id))
        laMesa = Mesa(self.mesaRepo.findById(id_mesa))
        elCandidato = Candidato(self.candidatoRepo.findById(id_candidato))
        elResultado.mesa = laMesa
        elResultado.candidato = elCandidato
        return self.resultadoRepo.save(elResultado)
    
    # Elimina un documento.
    def delete(self, id):
        return self.resultadoRepo.delete(id)
    
   ##########################
   ####### Consultas ########
   ##########################
   
    def getListarCandidatosMesa(self, id_mesa):
        return self.resultadoRepo.getListadoCandidatosInscritosMesa(id_mesa)

    def getListarMesasDeInscritoCandidato(self, id_candidato):
        return self.resultadoRepo.getListadoMesasCandidatoInscrito(id_candidato)

    def getMayorCedula(self):
        return self.resultadoRepo.getNumeroCedulaMayorCandidato()
    
    def getSumaVotosMesa(self):
        return self.resultadoRepo.getSumaVotosPorMesa()
    
    