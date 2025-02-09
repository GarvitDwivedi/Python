# Determine Whether the person is Child Teenage Adult senior 
key = int(input("Press 1 for Starting the game"))
while(key == 1 ):
    n = int(input("Enter the Age of Person"))
    if(n >0 and n <= 5):
        print("You are a Child")
    elif(n > 5 and n <= 17 ):
        print("You are a TeenAger")
    elif(n >= 18 and n <= 30):
        print("You are a Adult")
    else:
        print("You are a Senior Citizen")
    print("Do you want to playagain Press 1")
    print("Do you dont want to exit Press 0")
    key = int(input("Enter your Key"))
