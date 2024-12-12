import os
import time
import threading

global nice
global execution_time
global iteracoes

time_goal = 60
nice = 0
execution_time = 0

def gerador_processo(iteracoes):
    global nice, execution_time
    start = time.time()
    os.nice(nice)
    for i in range(iteracoes):
        i = i*i
    execution_time = time.time() - start
    print(f"Acabou! {execution_time:.2f} no nice: {nice} iteracoes: {iteracoes}")

def gerenciador_processos():
    global nice, execution_time, iteracoes

    if execution_time > time_goal:
        nice -= 3
        iteracoes -= 100
        print(f'[Lento] Tempo de execução: {execution_time:.2f}\nNovo nice: {nice}')
    elif execution_time < time_goal:
        nice += 3
        iteracoes += 100
        print(f'[Rápido] Tempo de execução: {execution_time:.2f}\nNovo nice: {nice}')

def executar_processos(iteracoes):
    global execution_time, nice
    
    while True:
        t1 = threading.Thread(target=gerador_processo, args=(iteracoes,))
        t2 = threading.Thread(target=gerenciador_processos)

        t1.start()
        t2.start()

        t1.join()
        t2.join()

        if time_goal - 1 < execution_time < time_goal + 1:
            break


iteracoes = 1_000_000_900
executar_processos(iteracoes)
