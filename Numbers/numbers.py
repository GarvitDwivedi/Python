# # x = 3 
# # y = 4 
# # z = 1 

# # # Basic Operators 

# # # print(x+ y) 
# # # print(x - y) 
# # # print(x *  y) 
# # # print(x /  y) 
# # # print(x //  y) 
# # # print(x %  y) 


# # # # precedence and associativity
# # # print(x + y * z )
# # # So how it is goung to be evaluated the precedence of * operator is greater than + so multiply will be 
# # # Evaluated first 
# # # X + y + z 
# # #x + 4 * 1 
# # # x + 4 
# # # 3 + 4 
# # # 7 

# # #precedence determines which operation is performed 
# # # first in an expression with more than one operator with different precedence 

# # # Operator associativity is used when two operators of the same precedence 
# # # appear in an expression. Associativity can be either from Left to Right or Right to Left

# # # But for industry these are not the best practices so just put a pair of parenthesis so that it 

# # print(x < y < z )
# # # so this can be understoood as 
# # print(x < y and y < z )

# # # AND VS OR 
# # #if any side in and is false then result is false 
# # #if any side is true in Or the result is true

# # # print(x < y and y < z)
# # # print(x < y or y < z)

# # # print(4 == 3) 
# # # print(3 == 3)
# # # print(3 != 3)
# # # print(3 != 8)

# a = 5.0 

# b = 5.0 

# a = 1 
# b = True

# print(a == b)
# print(a is b)

# print(3 + 5.0)

# print( 3 +  int(4.5))

# z = float(4 + 4 + int(21.22))
# print(z)

import random 

print(random.random())

print(random.randint(1,100))
x = (random.randint(1,1000))
print(random.random() * x)

l1 = ['a' , 'b' , 'c' , 'd']
print(random.choice(l1))

l1 = ['a' , 'b' , 'c' , 'd']
print(random.choices(l1) , 2)

print(0.1 + 0.1 + 0.1 - 0.3) #this is an issue here 

# so import a module called decimal 

import decimal 
print( decimal.Decimal(0.1) + decimal.Decimal(0.1) + decimal.Decimal(0.1) - decimal.Decimal(0.3))







