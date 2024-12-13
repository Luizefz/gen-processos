import os
import time
import threading
import queue

iteracoes = 60_000_900
time_goal = 60
progress = 0

def gerador_processo(fila, nice):
    print(f"pid gerador: {os.getpid()}")
    os.nice(nice)
    start_time = time.time()
    for i in range(iteracoes):
        progress = i
        i = i * i
        
        fila.put(progress)
    
    fila.put(None)  #Acabou a execução
    print(f"Acabou! Tempo de execução: {time.time() - start_time:.2f} segundos")

def gerenciador_processos(fila):
    pid = os.getpid()
    check_count = 0
    nice = 0
    while True:
        time.sleep(5)
        check_count += 1
        progress = fila.queue[-1]
        
        if progress is None:
            print("Parando a execução")
            break
        
        timer = check_count * 5

        if progress > 0:
            estimated_time = (iteracoes * timer) / progress
        else:
            estimated_time = float('inf')

        if estimated_time > time_goal:
            nice -= 3
            os.system(f"renice -n {nice} -p {pid}")
            print(f'[Lento] Estimado: {estimated_time:.2f}s, Novo nice: {nice}')
        elif estimated_time < time_goal:
            nice += 3
            os.system(f"renice -n {nice} -p {pid}")
            print(f'[Rápido] Estimado: {estimated_time:.2f}s, Novo nice: {nice}')
        else:
            print(f'[OK] Estimado: {estimated_time:.2f}s, Nice: {nice}')

fila = queue.Queue()

t1 = threading.Thread(target=gerador_processo, args=(fila, 0))
t2 = threading.Thread(target=gerenciador_processos, args=(fila,))

t1.start()
t2.start()

t1.join()
t2.join()
