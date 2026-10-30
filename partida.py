import random
from time import sleep

def simular_partida(time1, time2):
    gols1 = 0
    gols2 = 0
    nivelPartida = (time1.forca + time2.forca) // 2
    
    match nivelPartida:
        case nivelPartida if nivelPartida < 100:
            probabilidadeGol = 4500
        case nivelPartida if nivelPartida < 90:
            probabilidadeGol = 3500
        case nivelPartida if nivelPartida < 70:
            probabilidadeGol = 2000
        case nivelPartida if nivelPartida < 50:
            probabilidadeGol = 1000

    for i in range(90 + random.randint(0, 5)):
        if random.randint(1, probabilidadeGol) < time1.forca - (time2.forca // 1.6 + random.random()):
            gols1 += 1
        if random.randint(1, probabilidadeGol) < time2.forca - (time1.forca // 1.8 + random.random()):
            gols2 += 1
        #print(f"{time1.nome}: {gols1} | {time2.nome}: {gols2} || {i + 1} minutos")
    print(f"{time1.nome}: {gols1} | {time2.nome}: {gols2}\n{nivelPartida} de nível de partida\n")