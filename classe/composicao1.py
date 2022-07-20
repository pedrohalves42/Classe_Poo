from composicao import  Cliente

cliente1 = Cliente('Luiz',52)
cliente1.inserir_endereco('Bh','MG')
print(cliente1.nome)
cliente1.lista_enderecos()

cliente2 = Cliente('Joao',19)
cliente2.inserir_endereco('Sp','Sp')
cliente2.inserir_endereco('Bh','Mg')
print(cliente2.nome)
cliente2.lista_enderecos()

cliente3 = Cliente('Pedro',27)
cliente3.inserir_endereco('Salvador','Ba')
print(cliente3.nome)
cliente3.lista_enderecos()