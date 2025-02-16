def print_Kwargs(**kwargs):
    for key , value in kwargs.items():
        print(f"{key} , {value} " , end=" ")
    print(end="\n")




print_Kwargs(name = "Garvit" , Id = 29507)
print_Kwargs(name = "Garvit" , )
print_Kwargs(name = "Garvit" , Id = 29507 , rollNu = 2003480100026)