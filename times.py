import pickle

def selecionarLiga():
    while True:
        print()
        print("Selecione sua liga!")
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
        nomeLiga = int(input("\n Digite o número da liga que deseja selecionar: "))
        print("\n")
        try:
            with open(f'./dados/ligas/{ligas[nomeLiga - 1]}.pkl', 'rb') as times:
                liga = pickle.load(times)
                return liga
        except FileNotFoundError:
            print(f"Erro: Liga '{ligas[nomeLiga - 1]}' não encontrada.")
        except IndexError:
            print("Erro: Digite apenas os numeros das ligas mostradas")

def selecionarTime():
    liga = selecionarLiga()
    if not liga:
        return None
    
    print("Selecione seu time!")
    print("===================")
                
    for i in range(len(liga)):
        print(f"{i + 1}. {liga[i].nome}")
    
    nomeTime = int(input("Digite o número do time que deseja selecionar: "))
    print("\n")
    
    for time in liga:
        if time.nome == liga[nomeTime - 1].nome:
            return time
    
    return "Time não encontrado na liga.";

class Time():
    def __init__(self, nome, forcaDefesa, forcaMeio, forcaAtaque):
        self.nome = nome
        self.forca = [forcaDefesa, forcaMeio, forcaAtaque]