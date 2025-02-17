def print_even(n):
    for i in range(0 , n+1 , 2):
        yield i


n = 10 
for i in print_even(n):
    print(i)
    