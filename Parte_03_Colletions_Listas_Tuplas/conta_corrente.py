class ContaCorrente:
    
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0
    
    def deposita(self, valor):
        self.saldo += valor
        
    def __str__(self):
        return '[Codigo {} Saldo {}]'.format(self.saldo, self.codigo)
        
    
    conta_juh = ContaCorrente(15)
    print(conta_juh)
    
    conta_juh.deposita(500)
    print(conta_juh)
    
    conta_manu = ContaCorrente(761)
    conta_manu.deposita(1500)
    print(conta_manu)
    print('################')
    
    contas = [conta_juh, conta_manu]
    for conta in contas:
        print(conta)