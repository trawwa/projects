import threading
import time 

def thread_function(name):
    print(name, " - thread starting")
    time.sleep(2)
    print(name, " - after sleep")

if __name__ == "__main__":
    threads = []
    for index in range(3):
        print("create Thread - ", index)
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()
    
    for index, thread in enumirate(threads):
        print("before join - ", index)
        thread.join()
        print("after join - ", index)