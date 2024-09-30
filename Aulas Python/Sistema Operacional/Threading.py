import threading
import time


def contagem_1_a_5():
    for i in range (1, 6):
        print(f"Contagem 1 a 5: {i}")
        time.sleep(1) # Dorme por 1 segundo

def contagem_10_a_50():
    for i in range (10, 51, 10):
        print (f"Contagem 10 a 50: {i}")
        time.sleep(0.5) # Dorme por 0.5 segundos

# Criação de threads
thread1 = threading.Thread(target = contagem_1_a_5)
thread2 = threading.Thread(target = contagem_10_a_50)

# Inicialização das threads
thread1.start()
thread2.start()

# Aguarda a finalização das threads
thread1.join()
thread2.join()

print("Fim da execução")
