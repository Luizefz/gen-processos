import os
import time
import threading

time_goal = 5
pid_gerador = 0
# iteracoes = 1_000_000_000

# def gerador_processo_completo(valor_tempo):
#     # os.nice(-20)
#     for i in range(valor_tempo):
#         i = i*i


def gerador_processo_incompleto(iteracoes, nice):
    os.nice(nice)
    pid_gerador = os.getpid()
    for i in range(iteracoes):
        i = i*i

def gerenciador_processos(thread_processo_monitorado):
    execution_time = 0
    nice_value = 0

    start_time = time.time()
    while thread_processo_monitorado.is_alive():
        execution_time = time.time() - start_time

        if execution_time > time_goal:
            print(f'Tempo de execucao: {execution_time:.2f}\nNice: {nice_value}')

t1 = threading.Thread(target=gerador_processo_incompleto, args=(1_000_000_000, 10))
t2 = threading.Thread(target=gerenciador_processos, args=(t1))

t1.start()
t2.start()

t1.join()
t2.join()
