from random import randint as rt
class Pessoa:
    ano_atul = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nasc(self):
        print(self.ano_atul - self.idade)


    @staticmethod
    def gera_id():
        id = rt(10000, 19999)
        return id

print(Pessoa.gera_id())