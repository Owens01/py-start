"""modules"""
from math import sqrt,floor,acos

num=40

result = sqrt(num)
print(result)


""" function"""
def add():
    a=5
    b=2
    c=a-b
    print(c)

add()

"""how to get input from user/ swapping variable"""
a = input("Enter first num: ")
b = input("Enter second num: ")

# swapping
a, b = b, a

print("a:", a)
print("b:", b)
