arr = (input("ENter the value seperated by space").split())


for i in range(0,len(arr)):
    arr[i] = int(arr[i])

for i in arr:
    if i > 0:
        print(i)