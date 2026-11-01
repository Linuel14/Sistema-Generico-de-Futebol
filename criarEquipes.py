import pickle
import times

def criar_equipes():
    timesLiga = []
    nomeLiga = input("Digite o nome da sua liga: ")
    for i in range(0, int(input("Quantos times tem na sua liga? "))):
        timesLiga.append(times.Time(input("Nome do time: "), int(input("Força de defesa: ")), int(input("Força de meio: ")), int(input("Força de ataque: "))))
    with open(f'./dados/{nomeLiga}.pkl', 'wb') as arquivo:
        pickle.dump(timesLiga, arquivo)
    with open(f'./dados/ligas.pkl', 'ab') as arquivo:
        pickle.dump(nomeLiga, arquivo)