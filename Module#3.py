# Full Names
print("What are the names?")
names = input("Random Names seprated by comma: ")
names = names.split(",")

def random_names(x):
    print("Welcome to python, ")
    for names in x:
        print(names)
random_names(names)

def full_name(first, last):

    print("Hello", first, last)

full_name("Robert", "Moncrief")
full_name("Jeff", "Daniels")
full_name("Paul", "Moore")

# Addition Calculator
def addition_calc(x,y):
    sum = x + y
    print(x,"+",y,"=",sum)

addition_calc(75,10)
addition_calc(300,125)
addition_calc(25,13)

# Return Calculator
def return_calc(x,y):
    sum = x + y
    return(x+y)

print(return_calc(25,25))
print(return_calc(200,104))
print(return_calc(327,513))

# Consider the following expression

print(pow(16,(1/2)))

# 3) Define the variable x and y as lists of numbers, and z as a tuple
x = [1,2,3,4,5]
y = [11,12,13,14,15]
z = (21,22,23,24,25)

# a) What is the value of 3*x?
a = print(3*x)

# b) What is the value of x+y?
b = print(x+y)

# c) What is the value of x-y?
## This gave me an error, with some light research however i found it is possible to be calculated
import numpy as np
c = print(np.array([x]) - np.array([y]))

# d) What is the value of x[1]?
d = print(x[1])

# e) What is the value of x[0]?
e = print(x[0])

# f) What is the value of x[-1]?
f = print(x[-1])

# g) What is the value of x[:]?
g = print(x[:])

# h) What is the value of x[2:4]?
h = print(x[2:4])

# i) What is the value of x[1:4:2]?
i = print(x[1:4:2])

# j) What is the value of x[:2]?
j = print(x[:2])

# k) What is the value of x[::2]?
k = print(x[::2])

# l) What is the result of the following two expressions?
x[3]=8
print(x)

# m) What is the result of the above pair of expressions if the
# list x were replaced with the tuple z?
z[3]=8
print[z]


