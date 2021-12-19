# this file contains all the code for lecture 1

# How to get the data type of an variable?
i=1
print(type(i))

# How to get a random number



# Program to print hello world
print("Hello World!)

#program 2 - prints the version of Python we have

import sys
print(sys.version)

#program 3 - input radius of circle and get the area

radius = float(input("Enter the radius: "))
area = 3.14*radius*radius
print("The area of the circle is: ",area)

#program 4 - Input first and last name and print them in reverse order

firstname = input("Input first name: ")
secondname = input("Input second name: ")
print(secondname+' '+firstname)

#program 5 - Exercise: Write a program to input the value of n and getting n^3+n^2+n

n = int(input("Enter value of n: "))
print(n*n*n+n*n+n)

#program 6 - Exercise: Write a program to get the volume of sphere

r = int(input("Enter value of r: "))
print(4/3*3.14*r*r*r)



