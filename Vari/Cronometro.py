def cronometro(fun):
    
    def wrapper():
        import time
        start=time.time()
        fun()
        print(time.time()-start)
    return wrapper
@cronometro
def prova():
    print("ciao")

def prova2():
    print("hello")

prova=cronometro(prova)
prova=cronometro(prova2)
prova()


