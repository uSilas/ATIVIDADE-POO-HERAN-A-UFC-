class Conta:
    def __init__(self,clientes,número,saldo):
        self.saldo = saldo
        self.clientes = clientes
        self.número = número
        self.operações = []
        self.deposito(saldo)
        
    def resumo(self):
        for i,classe_cliente in enumerate(self.clientes):
            print(f"CC Número: {self.número} Saldo: {self.saldo:10.2f} Nome: {classe_cliente.nome} Telefone: {classe_cliente.telefone}")
    def saque(self, valor):
        if self.saldo < valor:
            print("tu não tem isso tudo de dinheiro não irmão")
            if self.saldo >= valor:
                self.saldo -= valor
                self.operações.append(["SAQUE", valor])
    def deposito(self,valor):
        self.saldo += valor
        self.operações.append(['SAQUE',valor])
    def extrato(self):
        print(f"Extrato CC Nº {self.número}\n")
        for o in self.operações:
            print(f"{o[0]:10s} {o[1]:10.2f}")
        print(f"\n Saldo: {self.saldo:10.2f}\n")
class ContaEspecial(Conta):
    def __init__(self,clientes,número,saldo=0,limite=0):
        Conta.__init__(self,clientes,número,saldo)
        self.limite = limite
    def saque(self,valor):
        if self.saldo + self.limite >= valor:
            self.saldo -= valor
            self.operações.append(["SAQUE", valor])