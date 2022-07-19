'''
setter = configurando um valor (=)
getter = obter um valor (.)
'''


class Pessoa:

    def __init__(self):
        self.nome = 'inicial'



    @property
    def nome(self):
        print('executado')
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome


    @property
    def sobrenome(self):
        return 'Desconhecido'


p1 = Pessoa()
p1.nome = 'Maria '
print(p1.nome)
print(p1.sobrenome)
