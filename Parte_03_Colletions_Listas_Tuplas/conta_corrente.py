from msilib.schema import Class


class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0
    
    def deposita(self, valor):
        self.saldo += valor
        
    def __str__(self):
        return '[Codigo {} Saldo {}]'.format(self.codigo, self.saldo)
        
    
conta_juh = ContaCorrente(15)
conta_juh.deposita(500)
print(conta_juh)
    
conta_manu = ContaCorrente(761)
conta_manu.deposita(1500)
print(conta_manu)
    
print('################')
    
contas = [conta_juh, conta_manu]
for conta in contas:
    print(conta)


def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

contas = [conta_juh, conta_manu]
print(contas[0], contas[1])
deposita_para_todas(contas)
print(contas[0], contas[1])

contas.insert(0,76)
print(contas[0], contas[1], contas[2])

#deposita_para_todas(contas)
#print(contas[0], contas[1], contas[2])

#### Tuplas

conta_juh = (15,2000)

def deposita(conta): # Variação funcional - separando o comportamento dos dados
    novo_saldo = conta[1] + 1000
    codigo = conta[0]
    return (codigo, novo_saldo)

deposita(conta_juh)

print('##############\n')

# Mesclando tuplas/listas

juh = ('Juliana', 34, 1987)
manu = ('Emanoela', 29, 1992)

usuarios = [juh, manu]
print(usuarios)

print('-----------')

usuarios.append(('Marcello', 33, 1988))
print(usuarios)

print('############\n')

# Herança e Polimorfismo

from abc import ABCMeta, abstractmethod

class Conta:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def deposita(self, valor):
        self._saldo += valor
    
    @abstractmethod #Obrigatorio implementar
    def passa_mes(self):
        pass
        
    def __str__(self):
        return '[Codigo {} Saldo {}]'.format(self._codigo, self._saldo)
    
print(Conta(88))

print('----------\n')

class ContaCorrente(Conta):
    
    def passa_mes(self):
        self._saldo -= 2
    
class ContaPoupanca(Conta):
    
    def passa_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

class ContaInvestimento(Conta):
    pass
    


conta17 = ContaCorrente(17)
conta17.deposita(150)
conta17.passa_mes()
print('Conta 17:', conta17)

conta19 = ContaPoupanca(19)
conta19.deposita(150)
conta19.passa_mes()
print('Conta 19:',  conta19)

print('----------\n')

conta17 = ContaCorrente(17)
conta17.deposita(150)
conta19 = ContaPoupanca(19)
conta19.deposita(150)
contas = [conta17, conta19]

for conta in contas:
    conta.passa_mes()
    print(conta)

print('\n############\n')

# Array e Numpy
import array as arr
print(arr.array('d',[1, 3.5]))


import numpy as np
numeros = np.array([1, 3.5])
print(numeros)

numeros += 3
print(numeros)


print('\n############\n')

# Equals __eq__

class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def __eq__(self, other):
       return self._codigo == other._codigo
    
    def deposita(self, valor):
        self._saldo += valor
        
    def __str__(self):
        return "[Codigo {} Saldo {}]".format(self._codigo, self._saldo)
    
conta1 = ContaSalario(37)
conta2 = ContaSalario(37)

conta1 == conta2

print('\n-------------\n')

class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def __eq__(self, other):
       return self._codigo == other._codigo and self._saldo == other._saldo
    
    def deposita(self, valor):
        self._saldo += valor
        
    def __str__(self):
        return "[Codigo {} Saldo {}]".format(self._codigo, self._saldo)

conta1 = ContaSalario(37)
conta2 = ContaSalario(37)
conta1 == conta2

#conta1.deposita(5)

print(conta1 == conta2)

print('\n-------------\n')

class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo and self._saldo == other._saldo
    
    def deposita(self, valor):
        self._saldo += valor
        
    def __str__(self):
        return "[Codigo {} Saldo {}]".format(self._codigo, self._saldo)
    

conta1 = ContaSalario(37)
conta2 = ContaCorrente(37)
print(conta1 == conta2)

print(isinstance(ContaCorrente(34), Conta))

print('\n-------------\n')

class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo and self._saldo == other._saldo
    
    def deposita(self, valor):
        self._saldo += valor
        
    def __str__(self):
        return "[Codigo {} Saldo {}]".format(self._codigo, self._saldo)

class MultiploSalario(ContaSalario):
    pass

conta1 = ContaSalario(37)
conta2 = ContaCorrente(37)
print(conta1 == conta2)

print('\n############\n')

# Range/len/enumerate

idades = [15, 87,32, 65, 56, 32, 49, 37]
for i in range(len(idades)):
    print(i, idades[i])

list(enumerate(idades))

for valor in enumerate(idades):
    print(valor)

for indice, idade in enumerate(idades):
    print(indice, 'X', idade)
    
usuarios = [
    ('Juliana', 34, 1987),
    ('Emanoela', 29, 1992),
    ('Marcello', 33, 1988)
]

for nome, idade, nascimento in usuarios: #unpack
    print(nome)
    
for nome, _, _ in usuarios: #unpack ignorando os demais
    print(nome)

print('\n############\n')

#Ordenação

print(idades)
print(sorted(idades, reverse=True))
idades.sort()
print(idades)

print('\n-------------\n')

class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo and self._saldo == other._saldo
    
    def deposita(self, valor):
        self._saldo += valor
        
    def __str__(self):
        return "[Codigo {} Saldo {}]".format(self._codigo, self._saldo)
    
conta_juh = ContaSalario(7461)
conta_juh.deposita(1000)

conta_manu = ContaSalario(645)
conta_manu.deposita(1500)

conta_marcello = ContaSalario(7891)
conta_marcello.deposita(1300)

contas = [conta_juh, conta_manu, conta_marcello]

for conta in contas:
    print(conta)

print('\n-------------\n')

def extrai_saldo(conta):
    return conta._saldo

for conta in sorted(contas, key=extrai_saldo):
    print(conta)

print('\n-------------\n')

from operator import attrgetter

for conta in sorted(contas, key=attrgetter('_saldo')):
    print(conta)
    
    
print('\n-------------\n')

class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo and self._saldo == other._saldo
    
    def __lt__(self, other):
        return self._saldo < other._saldo
    
    def deposita(self, valor):
        self._saldo += valor
        
    def __str__(self):
        return "[Codigo {} Saldo {}]".format(self._codigo, self._saldo)
    
conta_juh = ContaSalario(7461)
conta_juh.deposita(1000)

conta_manu = ContaSalario(645)
conta_manu.deposita(1500)

conta_marcello = ContaSalario(7891)
conta_marcello.deposita(1300)

contas = [conta_juh, conta_manu, conta_marcello]

conta_juh > conta_marcello
conta_marcello > conta_manu
conta_manu > conta_juh

for conta in sorted(contas):
    print(conta)

print('\n-------------\n')

conta_juh = ContaSalario(7461)
conta_juh.deposita(1300)

conta_manu = ContaSalario(645)
conta_manu.deposita(1500)

conta_marcello = ContaSalario(7891)
conta_marcello.deposita(1300)

contas = [conta_juh, conta_manu, conta_marcello]

for conta in sorted(contas, key=attrgetter('_saldo', '_codigo')):
    print(conta)


print('\n----------------n')

class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo and self._saldo == other._saldo
    
    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        return self._codigo < other._codigo
    
    def deposita(self, valor):
        self._saldo += valor
        
    def __str__(self):
        return "[Codigo {} Saldo {}]".format(self._codigo, self._saldo)
    

conta_juh = ContaSalario(7461)
conta_juh.deposita(1500)

conta_manu = ContaSalario(645)
conta_manu.deposita(1500)

conta_marcello = ContaSalario(7891)
conta_marcello.deposita(1500)

contas = [conta_juh, conta_manu, conta_marcello]

#Ordenado por codigo da conta menor quando saldos forem iguais
for conta in sorted(contas):
    print(conta)
    

print('\n----------------n')

#Ordenação functools 
from functools import total_ordering

@total_ordering
class ContaSalario:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def __eq__(self, other):
        if type(other) != ContaSalario:
            return False
        return self._codigo == other._codigo and self._saldo == other._saldo
    
    def __lt__(self, other):
        if self._saldo != other._saldo:
            return self._saldo < other._saldo
        return self._codigo < other._codigo
    
    def deposita(self, valor):
        self._saldo += valor
        
    def __str__(self):
        return "[Codigo {} Saldo {}]".format(self._codigo, self._saldo)
    

conta_juh = ContaSalario(7461)
conta_juh.deposita(1000)

conta_manu = ContaSalario(645)
conta_manu.deposita(1500)

conta_marcello = ContaSalario(7891)
conta_marcello.deposita(1300)

contas = [conta_juh, conta_manu, conta_marcello]

print(conta_juh <= conta_manu)


#Ordenado total com criterio de igualdade tbm
