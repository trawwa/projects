import threading
import time 

def thread_function(name):
    print(name, " - thread starting")
    time.sleep(2)
    print(name, " - after sleep")

if __name__ == "__main__":
    print("before create Thread")
    x = threading.Thread(target=thread_function, args=(1,))
    print("before running Thread")
    x.start()
    print("Wait thread finish")
    ##x.join()
    print("all done")