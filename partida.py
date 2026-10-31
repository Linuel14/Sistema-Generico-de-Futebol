import random
from time import sleep

def simular_partida(time1, time2):
    gols1 = 0
    gols2 = 0
    finalizacoes1 = 0  
    finalizacoes2 = 0
    nivelPartida = ((sum(time1.forca) // 3) + (sum(time2.forca) // 3)) // 2
    
    #match nivelPartida:
     #   case nivelPartida if nivelPartida < 100:
      #      probabilidadeGol = 4500
       #     probabilidadeFinalizacao = 800
        #case nivelPartida if nivelPartida < 90:
         #   probabilidadeGol = 3500
        #    probabilidadeFinalizacao = 200
        #case nivelPartida if nivelPartida < 70:
        #    probabilidadeGol = 2000
        #    probabilidadeFinalizacao = 200
        #case nivelPartida if nivelPartida < 50:
        #    probabilidadeGol = 1000
        #    probabilidadeFinalizacao = 100
    
    if nivelPartida > 90:
        probabilidadeGol = 3500
        probabilidadeFinalizacao = 500
    elif nivelPartida > 80:
        probabilidadeGol = 2000
        probabilidadeFinalizacao = 450
    elif nivelPartida > 70:
        probabilidadeGol = 2000
        probabilidadeFinalizacao = 300
    elif nivelPartida > 60:
        probabilidadeGol = 1000
        probabilidadeFinalizacao = 250
    else:
        probabilidadeGol = 1000
        probabilidadeFinalizacao = 150

    for i in range(90 + random.randint(0, 5)):
        if random.randint(1, probabilidadeFinalizacao) < time1.forca[1] - (time2.forca[0] // 2):
            finalizacoes1 += 1
            if random.randint(1, probabilidadeGol) < time1.forca[2] - (time2.forca[0] // 1.6 + random.random()):
                gols1 += 1
        if random.randint(1, probabilidadeFinalizacao) < time2.forca[1] - (time1.forca[0] // 2):
            finalizacoes2 += 1
            if random.randint(1, probabilidadeGol) < time2.forca[2] - (time1.forca[0] // 1.6 + random.random()):
                gols2 += 1
        
        print(f"{time1.nome}: {gols1} | {time2.nome}: {gols2} || {i + 1} minutos", end="\r")
        #sleep(0.1)
    print(f"{finalizacoes1} finalizações de {time1.nome} e {finalizacoes2} finalizações de {time2.nome}\n {nivelPartida} de nível da partida")