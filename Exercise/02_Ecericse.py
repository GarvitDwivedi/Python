day = input("Enter the Day")
age = int(input("Enter your age"))

if(age >= 18):
    if(day == "wednesday"):
        print("The cost is " , 12 - (12*0.2))
    else:
        print("The cost is " , 12)
else:
    if(day == "wednesday"):
        print("The cost is " , 8 - (8 * 0.2))
    else:
        print("The cost is " , 8 )