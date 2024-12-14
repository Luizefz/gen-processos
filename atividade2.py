import os
import time

def funcao(valor_temp):
	for i in range(valor_temp):
		i=i*i

valor = 150_000_500	#Escolher o valor de forma que demore 60s para ser executado
start = time.time()
funcao(valor)
print(f"Tempo atual: {time.time()-start:.2f}")