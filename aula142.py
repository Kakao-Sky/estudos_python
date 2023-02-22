# Classes abstratas - Abstract Base Class (abc)
# ABCs são usadas como contratos para a definição de novas classes.
# Elas podem forçar outras classes a criarem métodos concretos. 
# Também podem ter métodos concretos por elas mesmas. 
# @abstractmethods são métodos que não têm corpo.
# As regras para classes abstratas com métodos abstratos é que elas NÃO PODEM ser instâncias diretamente.
# Métodos abstratos DEVEM ser implementados nas subclasses (@abstractmethod).
# Uma classe abstrata em Python tem sua metaclasse sendo ABCMeta.
# É possível criar @property, @setter, @classmethod, @staticmethod e @method como abstratos,
# para isso, use @abstractmethod como decorador mais interno.

from abc import ABC, abstractmethod # ABC é uma classe, você importa normalmente dela 
# from abc import ABC, ABCMeta  

# class Log(metaclass=ABCMeta): # outra forma de criar uma classe abstrata, significa o mesmo da linha abaixo
class Log(ABC): # pra tornar essa classe abstrata, eu herdo da classe ABC
    @abstractmethod # com isso, a classe fica totalmente abstrata e começa a dar erro no "l = Log()"
    def _log(self, msg): ... # PRECISA SER IMPLEMENTADO NAS SUBCLASSES(o método abstrato)
        # esse método não tem corpo, é abstrato

    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')

#############################################################################################################

class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')

# LogPrintMixin herda de Log, que por sua vez, herda de ABC

# l = Log() # se não der um erro nessa linha, significa que a classe não é, de fato, abstrata

# para uma classe ser abstrata, ela precisa ter, pelo menos, um método abstrato, independente de quantos 
# métodos ela tenha, pelo menos um precisa ser abstrato

# Após a classe se tornar TOTALMENTE ABSTRATA,  a única forma de utilizar ela é através das instâncias das
# classes que herdaram ela (nesse caso, LogPrintMixin) 
l = LogPrintMixin() # instância da classe filha LogPrintMixin()
l.log_error('Agora estou usando um método concreto da classe Log()')
