from cliente import Cliente
from contas import Conta,ContaEspecial

joão = Cliente("João", "777-1234")
maria = Cliente("Maria", "555-4321")
conta1 = Conta([joão],1,1000)
conta2 = ContaEspecial([maria,joão],2,500,1000)
conta1.saque(50)
conta2.deposito(300)
conta1.saque(190)
conta2.deposito(95.15)
conta2.saque(1500)
conta1.extrato()
conta2.extrato()