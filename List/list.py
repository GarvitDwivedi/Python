# list1  =[1,2,3,4,5,6]
# print(list1[1])

# list1[0] = 544

# print(list1)

# list2 = list1 
# list1[0] = 33 
# list1[5] = 33 
# print(list1)
# print(list2)
username = ["Garvit" , "Gaurav" , "Ashu" , "Golu"]
# print(username[0:2])

# print(username[1:1])

# username[1:1] = "Jalal" #this will insert every value as list 


# print(username)

# username[1:3] = ["Abd" , "Maha"]
# print(username)



# username[3:3] = ["Abd" , "Maha"]
# print(username)
username.append("NEW")# used to add item at the last of 
print(username)

username.pop()  #Remove item from the end 
print(username)

username.sort() 
print(username)

# newusername = username #these two will point to the same address 
#if we want them to have different coppies so we can do this by .copy method

newusername = username.copy() 
newusername[0] = 5 
print(newusername , username)