t1 = (1,2,3,4,5)
print(t1)
t2 = t1 
t2.count(4)
print(t1.count(2))

print(t2.__len__())

print(t2[4])
#t2[4] = 4 # Not allowed as tuple are immutable these are made to as a immutalbe subsitute of list in python