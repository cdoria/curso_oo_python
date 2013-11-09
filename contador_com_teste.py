"""
>>> ca = ContadorAmigavel()
>>> for letra in 'araquara':
...    ca.incrementar(letra)
>>> ca.contagem('a')
4
>>> ca.contagem('q')
1
>>> ca.contagem('z')
0
>>> ct = ContadorTotalizador()
>>> for letra in 'banana':
...    ct.incrementar(letra)
>>> ct.total
6

>>> round(ct.porcentagem('n'), 1)
33.3
>>> round(ct.porcentagem('b'), 1)
16.7

>>> cta = ContadorTotalizadorAmigavel()
>>> for letra in 'laranja':
...    cta.incrementar(letra)
>>> cta.total
7
>>> cta.contagem('a')
3
>>> cta.contagem('x')
0
>>> round(cta.porcentagem('a'), 1)
42.9
>>> round(cta.porcentagem('x'), 1)
0.0
"""

class Contador:

    def __init__(self):
        self.ocorrencias = {}

    def incrementar(self, item):
        qtd = self.ocorrencias.get(item, 0) + 1
        self.ocorrencias[item] = qtd

    def contagem(self, item):
        return self.ocorrencias[item]
    
class ContadorAmigavel(Contador):

    def contagem(self, item):
        self.ocorrencias[item] = self.ocorrencias.get(item,0)
        return self.ocorrencias[item]


class ContadorTotalizador(Contador):
       
    def __init__(self):
        Contador.__init__(self)
        self.total = 0
        
    def incrementar(self, item):
        Contador.incrementar(self, item) #Por que aqui teve que invocar a classe
        self.total +=1

    def porcentagem(self, item):
        return (ContadorAmigavel.contagem(self, item)/self.total)*100

class ContadorTotalizadorAmigavel(ContadorAmigavel, ContadorTotalizador):
    """Será que é só isso ?"""



