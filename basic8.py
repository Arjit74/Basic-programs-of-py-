#WAP to find the area of triangle using Heron's formula.
import math as m
a = int(input ("Enter the first side:- "))
b = int(input ("Enter the second side:- "))
c = int(input ("Enter the third side:- "))
s = (a+b+c)/2
are = m.sqrt(s*(s-a)*(s-b)*(s-c))
print("Area of the triangle is :- ",are) 
