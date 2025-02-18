def fun(n):
    print(n)
    def fun1():
        print(n)
    fun1()



fun(4)


x = 77 
print(x)

def new():
    print(x)


def newfun():
    global x 
    x= 5 
    print(x)



print(x)
newfun()
print(x)
    
