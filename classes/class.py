class student:
    def __init__(self , name , id):
        self.name = name 
        self.id = id 
    
    def printDetail(self):
        print(self.name , "---->" , self.id)


s1  = student("Garvit" , 29507)
s2  = student("Gaurav" , 29094)

print(s1.name)
print(s1.id)
(s1.printDetail())
        


print(s2.name)
print(s2.id)