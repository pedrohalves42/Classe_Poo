'''
public, rotected, private
'''


class BaseDados:
    def __init__(self):
        self._dados = {}

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self._dados:
            self._dados["clientes"] = {id: nome}
        else:
            self._dados["clientes"].update({id: nome})

    def lista_clientes(self):
        for id, nome in self._dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self,id):
        del self._dados['clientes'][id]



bd = BaseDados()
bd.inserir_cliente(1, 'otavio')
bd.inserir_cliente(2, 'Camargo')
bd.inserir_cliente(3, 'Maria')
#bd.lista_clientes()
bd.apaga_cliente(1)
#bd.lista_clientes()
bd.inserir_cliente(1,'Marcos')
bd.lista_clientes()
