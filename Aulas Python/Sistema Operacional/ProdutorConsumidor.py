import threading
import time
import random
from queue import Queue

# Buffer compartilhado entre o produtor e o consumidor
buffer = Queue(maxsize = 5)

# Produtor
def Produtor():
    while True:
        # Produzir um item
        item = random.radint(1, 100)
        # Simular o tempo de produção
        time.sleep(random.randint(1, 3 ))

        # Adicionar o item ao buffer
        buffer.put(time)
        print(f"Produtor gerou o item {item}. Buffer atual: {buffer.qsize()} itens")

# Consumidor
def Consumidor():
    while True:
        # Simular o tempo de produção
        time.sleep(random.randint(1, 3 ))

        # Consumir o item
        item  =buffer.get()
        print(f"Consumidor consumiu o item {item}. Buffer atual: {buffer.qsize()} itens")
        buffer.task_done() # Sinaliza que o item foi processado

# Criando as threads  para simular o produtor e o consumidor
produtor_thread = threading.Thread(target=Produtor)
consumidor_thread = threading.Thread(target=Consumidor)

# Iniciando as threads
produtor_thread.start()
consumidor_thread.start()

#Garantir que as threads não terminem
produtor_thread.join()
consumidor_thread.join()

print("Execução finalizada")