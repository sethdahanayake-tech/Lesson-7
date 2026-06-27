# Write a program to illustrate the use of 'is' identity operator
# Python program to illustrate the use

# of 'is' identity operator


x = 5

if (type(x) is int):

    print("true")

else:

    print("false")


x = 5.5

if (type(x) is float):

    print("true")
y = 30

if x is y:

    print("true")

    