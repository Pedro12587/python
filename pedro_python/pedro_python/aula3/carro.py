
class Carro:

    # Configuração inicial do objeto
    def __init__(self, nome, cor, modelo, ano, marca):
        # Definir atributo
        self.nome = nome
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.marca = marca

    def correr(self):
        print("correndo muito.........")

    def frear(self):
        print("freiando......... pastilha está ruim.....")

    def ligar(self):
        print("ligando o carro.........",self.nome)

passatcarro = Carro("Passat", "Preto", "V1", "2025", "volkswagen")
passatcarro.ligar()

passatcarro.correr()
passatcarro.frear()


