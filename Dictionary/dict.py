dict = {1:"A" , 2 : "B" , 3 : "C" }
print(dict)

print(dict[1])

for it in dict :
    print(it , dict[it])


if 5 in dict :
    print("Yes")
else:
    print("No")

new_dict = {1 : {"Garvit" : "Dwivedi" , "Gaurav" : "Singh"  } , 2 : {"Abhimanyu" : "Arjun"  , "New"  : "Person"}}
print(new_dict)

print(new_dict[1]["Garvit"])

dict[1] = "Garvit"
print(dict)

dict.popitem()
print(dict)

dict.popitem()
print(dict)

dict[6] = "Garvit"
print(dict)


# newdict3 = dict + new_dict
# print(newdict3)/


for key , vlaue in dict.items():
    print(key , vlaue)

