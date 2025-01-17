class cidade:
    def __init__(self,nome,populacao):
        self.nome = nome
        self.populacao = populacao
        
class estado:
    def __init__(self,nome,sigla,cidades):
        self.nome = nome
        self.sigla = sigla
        self.cidades = cidades

    def populacao_soma(self):
        soma = 0
        for index,cidade in enumerate(cidades):
            soma = cidade.populacao + soma
        print(f"O estado {self.nome}({self.sigla}) tem uma populacao de {soma} habitantes")


itapaje = cidade("Itapaje",50000)
fortaleza = cidade("Fortaleza",1000000)
tururu = cidade("cidade do rick bessa", 1)
cidades = [itapaje,fortaleza,tururu]
ceara = estado("Ceará","CE",cidades)
ceara.populacao_soma()

