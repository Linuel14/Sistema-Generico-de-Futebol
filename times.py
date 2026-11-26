import pickle

def selecionarLiga():
    while True:
        print("\nSelecione sua liga!")
        print("=============================")
        with open('./dados/ligas.pkl', 'rb') as arquivo:
            ligas = []
            while True:
                try:
                    liga = pickle.load(arquivo)
                    ligas.append(liga)
                except EOFError:
                    break
            
        for i in range(len(ligas)):
            print(f"{i + 1}. {ligas[i]}")
        print("=============================")
        nomeLiga = int(input("\nDigite o número da liga que deseja selecionar: "))
        print()
        try:
            with open(f'./dados/ligas/{ligas[nomeLiga - 1]}.pkl', 'rb') as times:
                liga = pickle.load(times)
                return liga
        except IndexError:
            print("Erro: Digite apenas os numeros das ligas mostradas")

def selecionarTime():
    liga = selecionarLiga()
    while True:
        try:
            print("\nSelecione seu time!")
            print("=============================")
                        
            for i in range(len(liga)):
                print(f"{i + 1}. {liga[i].nome}")
            print("=============================")
            nomeTime = int(input("\nDigite o número do time que deseja selecionar: "))
            print()
            
            for time in liga:
                if time.nome == liga[nomeTime - 1].nome:
                    return time
        except IndexError:
            print("Erro: Digite apenas os numeros dos times mostrados")

class Time():
    def __init__(self, nome, forcaDefesa, forcaMeio, forcaAtaque):
        self.nome = nome
        self.forca = [forcaDefesa, forcaMeio, forcaAtaque]