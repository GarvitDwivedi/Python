def sum(*args):
    sum = 0 
    for i in args:
        sum += i 
    return sum 


print(sum(1,2,3,4))
print(sum(1,2,3,4,3,4,7,8))
print(sum(1,2,3,4,5,534,635,3))
print(sum(1,2,3,4 ,3,45,4,24,2))


# *args is used to accept multiple parameter as many as proided by the user