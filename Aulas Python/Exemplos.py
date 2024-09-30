import threading
import time
import random

# Variáveis globais
espera = 0
cadeiras = 3
barbeiro_dormindo = threading.Semaphore(0)
mutex = threading.Lock()

#Função que simula o corte de cabelo
def cortar_cabelo():
    print("o barbeiro está cortando o cabelo...")
    time.sleep(random.randint(1, 5)) #Simular o tempo de corte de cabelo
    print("o barbeiro terminou o corte de cabelo")

#Função do barbeiro
def barbeiro():
    global espera
    while True:
        #Espera até que  haja um cliente para cortar o cabelo
        barbeiro_dormindo.acquire()

        with mutex:
            espera -= 1 #Decrementa o número de clientes esperando
            
        cortar_cabelo() #corta o cabelo do cliente

# Função do cliente
def cliente(cliente_id):
    global espera

    #Cliente entrar na barbearia
    with mutex:
        if espera < cadeiras:
            espera += 1
            print (f"Cliente {cliente_id} está esperando...  Clientes na fila: {espera}")

            barbeiro_dormindo.release() #Acordar o barbeiro caso esteja dormindo
        else:
            print("Cliente {cliente_id} foi embora, pois  a barbearia está cheia!")

#Função principal
def simular_barbearia():
    threading.Thread(target=barbeiro).start() #Inicia a thread  do barbeiro

    cliente_id = 1
    while True:
        time.sleep(random.randint(1, 5))
        threading.Thread(target=cliente, args=(cliente_id,)).start()

        cliente_id += 1

simular_barbearia()