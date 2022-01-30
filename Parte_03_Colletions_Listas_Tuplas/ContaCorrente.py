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

class Conta:
    def __init__(self, codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def deposita(self, valor):
        self._saldo += valor
        
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