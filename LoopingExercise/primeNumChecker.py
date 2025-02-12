n = int(input("Enter the Number"))


isPrime = True

for i in range(2 , n):
    if(n % i == 0):
        isPrime = False 

if(isPrime):
    print("Entered Number is a Prime Number")
else:
    print("Entered Number is Not a Prime Number")
    
