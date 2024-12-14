import os
import time
import threading
import queue

global progress
global end_counting

iteracoes = 350_000_500	
time_goal = 60
progress = 0
end_counting = False

def gerador_processo(iteracoes_params, nice):
    global end_counting
    global progress
    os.nice(nice)
    for i in range(iteracoes_params):
        progress += 1
        i = i * i

    end_counting = True 

def gerenciador_processos(iteracoes_params):
    global progress
    pid = os.getpid()
    check_count = 0
    nice = 0
    start_time = time.time()

    while not end_counting:
        check_count += 1
        
        
        timer = ((time.time() - start_time) * 100) / 60
        iteracoes_percent = (progress * 100) / iteracoes_params

        # if progress == 100:
        #     print("Parando a execução")
        #     break
       
        if timer > iteracoes_percent:
            nice = max(nice - 1, -20)
            os.system(f"renice -n {nice} -p {pid}")
            print(f'[Lento] Timer - {timer:.2f} iteracoes - {iteracoes_percent:.2f}%, Novo nice: {nice}')

        elif timer < iteracoes_percent:
            nice = min(nice + 1, 19)
            os.system(f"renice -n {nice} -p {pid}")
            print(f'[Rapido] Timer - {timer:.2f} iteracoes - {iteracoes_percent:.2f}%, Novo nice: {nice}')

        else:
            print(f'[OK] Estão parelhos: timer - {timer:.2f}% iteracoes - {iteracoes_percent:.2f}%, Nice: {nice}')

    print(f'Tempo de execução {time.time() - start_time}')

fila = queue.Queue()

t1 = threading.Thread(target=gerador_processo, args=(iteracoes, 0))
t2 = threading.Thread(target=gerenciador_processos, args=(iteracoes,))

t1.start()
t2.start()

t1.join()
t2.join()
