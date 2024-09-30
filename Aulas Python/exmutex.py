import threading

mutex = threading.Lock()

def thread_function():
    mutex.acquire()
    try:
        print("Thread", threading.current_thread().name, "acessou o recurso compartilhado!")
    finally:
        mutex.release()

t1 = threading.Thread(target=thread_function) 
t2 = threading.Thread(target=thread_function)

t1.start()
t2.start()

t1.join()
t2.join()