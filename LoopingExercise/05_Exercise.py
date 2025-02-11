s = input("Enter a String ")

def helper(ch , s):
    cnt = 0 
    for i in range(0 , len(s)):
        if(s[i] == ch):
            cnt+=1
    return cnt 
    


for i in range(0 , len(s)):
    if(helper(s[i] , s) == 1):
        print(s[i])
        break 


#Using Dictionary
dict = {} 
for i in range(0 , len(s)):
    if s[i] in dict:
        dict[s[i]]+=1
    else:
        dict[s[i]] = 1 

for i in range(0 , len(s)):
    if(dict[s[i]] == 1):
        print(s[i])
        break ; 


