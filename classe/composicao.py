class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idadade = idade
        self.enderecos = []

    def inserir_endereco(self, cidade, estado):
        self.enderecos.append(Endereco(cidade, estado))

    def lista_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.cidade, endereco.estado)

    def __del__(self):
        print(f'{self.nome} Foi apagado')


class Endereco:
    def __init__(self, cidade, estado):
        self.cidade = cidade
        self.estado = estado

    def __del__(self):
        print(f'{self.estado}/{self.cidade} Endereco apagado ')
