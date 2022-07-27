'''
Associação - Usa | Agragação - Tem | Composição - E dono | Herança - E
'''
import classe
from classe.heranca1 import Cliente, Aluno
from classe.pessoa import Pessoa

c1 = Cliente('Luiz',45)
print(c1.nome)

a1 = Aluno('Maria',32)
