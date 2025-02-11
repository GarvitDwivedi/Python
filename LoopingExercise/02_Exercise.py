arr = input("Enter the element with sapce").split() 

for i in range(0 , len(arr)):
    arr[i] = int(arr[i])

sum = 0 
for i in arr:
    if( i  % 2 == 0):
        sum += i 

print(sum)
