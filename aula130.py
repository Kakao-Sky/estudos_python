# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)

class Connection:
    
    # method -> método de instância -> acesso ao self
    def __init__(self, host='localhost'): 
        # inicializa os atributos da instância
        self.host = host
        self.user = None
        self.password = None
        
    def set_user(self, user):
        # setter 
        self.user = user

    def set_password(self, password):
        # setter 
        self.password = password

    @classmethod # tem acesso ao cls
    def create_with_auth(cls, user, password):
        connection = cls() # tá recebendo a referência da classe Connection()
        connection.user = user
        connection.password = password
        return connection

    @staticmethod # não tem acesso ao self, nem ao cls
    def log(msg):
        print('LOG: ', msg)


# c1 = Connection()
c1 = Connection.create_with_auth('carol', 12346)
# print(c1.user)
# c1.set_user('Carroline')
# c1.set_password('123456')
print(c1.user)
print(c1.password)
Connection.log('Mensagem de log')
