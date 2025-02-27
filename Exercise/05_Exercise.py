def iseven(n):
    if(n % 2 == 0):
        return True
    return False

n = int(input("Enter the Number"))
if iseven(n):
    print("Even")
else:
    print("Odd")