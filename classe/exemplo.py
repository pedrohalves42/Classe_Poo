class Pessoa:
    ano_atul = 2022

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def get_ano_nasc(self):
        print(self.ano_atul - self.idade)

    @classmethod
    def por_ano_nasc(cls, nome, ano_nascimento):
        idade = cls.ano_atul - ano_nascimento
        return cls(nome, idade)


#p1 = Pessoa.por_ano_nasc('luiz', 1987)
p1 = Pessoa('maria',29)
print(p1.nome)
print(p1.idade)
p1.get_ano_nasc()
