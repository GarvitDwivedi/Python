n = int(input("Enter the number"))

if(n % 2 != 0):
    print("Odd Number")
else:
    print("Even Number")
res = "Even" if n % 2 == 0 else "Odd"
print(res)


