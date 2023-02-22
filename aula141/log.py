# Arquivo de Log
# Abstração

from pathlib import Path # Parte 3

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log: 
    # esse método log() só existe pra definir que existe o método log na classe Log
    # padrão de projeto - Template Method
    def _log(self, msg): # assinatura do método
        raise NotImplementedError('Implemente o método log') # abstração -> eu não quero que 
        # uma pessoa utilize essa classe diretamente,
        #  eu quero que ela utilize a subclasse
        # NotImplementedError -> significa que está usando uma classe que não deveria ser usada

    def log_error(self, msg): # Parte 2
        return self._log(f'Error: {msg}')
        # self.log -> faz referência ao self e ao método log() da classe em que vai ser chamado
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')

class LogFileMixin(Log):
    # mixin -> estou falando p/ outros desenvolvedores adicionarem funcionalidades na sua herança múltipla
    # ou seja, é para adicionar coisas dentro das outras classes, não dentro da família do seu objeto 
    # mixin -> é uma classe que tem funcionalidades que serão adicionadas em outras classes,
    # que podem não ser dessa família
    def _log(self, msg): # se está sobrepondo um método, assinaturas devem ser IGUAIS
        print(msg)
        msg_formatada = f'{msg} ({self.__class__.__name__})'
        print(f'Salvando: {msg_formatada}')
        with open(LOG_FILE, 'a') as arquivo:
            arquivo.write(msg_formatada)
            arquivo.write('\n')

    # log_error pode ser acessado aqui tbm, e vai chamar o mét. log daqui e o self daqui



class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')



if __name__ == '__main__':
    lp = LogPrintMixin()
    lp.log_error('Mensagem de erro do LogPrint')
    lp.log_success('Mensagem de sucesso LogPrint')

    lf = LogFileMixin()
    lf.log_error('Mensagem de erro do LogFile')
    lf.log_success('Sucesso LogFile')
    # print(LOG_FILE)