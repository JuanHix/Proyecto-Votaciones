from abc import ABCMeta 

# Clase Abstracta "Padre" para creacion de modelos. 
class AbstractModelo(metaclass=ABCMeta): 
    def __init__(self,data): 
        for llave, valor in data.items(): 
            setattr(self, llave, valor)
            