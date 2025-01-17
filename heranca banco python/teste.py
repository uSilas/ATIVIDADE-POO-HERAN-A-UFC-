from cliente import Cliente
from contas import Conta
joão = Cliente("João da Silva", "777-1234")
maria = Cliente("Maria Silva","555-4321")
jose = Cliente("Cliente","777-666")

conta1 = Conta([joão],1,1000)
conta2 = Conta([maria,joão],2,500)
conta3 = Conta([joão,jose],3,500)
contas_list = [conta1,conta2]

conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(250)
conta1.resumo()
conta2.resumo()
conta3.resumo()
conta1.extrato()
conta2.extrato()
conta3.extrato()

#criando objetos e utilizando banco:
from banco import Banco

contaJM = Conta([joão,maria],4,100)
contaJ = Conta([jose],5,10)
tatu = Banco("Tatú")
tatu.abre_conta(contaJM)
tatu.abre_conta(contaJ)
tatu.lista_contas()


