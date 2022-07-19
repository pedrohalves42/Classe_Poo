from associacao import Escritor
from associacao import Caneta
from associacao import MaquinaDeEscrever
'''
escritor = Escritor('Joao')
print(escritor.nome)
caneta = Caneta('Bic')
maquina = MaquinaDeEscrever()
print(caneta.marca)
maquina.escrever()
'''
escritor = Escritor("Pedro")
caneta = Caneta("bic")
maquina = MaquinaDeEscrever()

escritor.ferramenta = maquina
escritor.ferramenta.escrever()

