#WAP that take sthe users age as input and determine if they are eligible to vote (above 18).
a= int(input("Enter the age to be checked:- "))
b= (a>=18)*"The candidate is eligible for voting" + (a<18)*"The candidate is not eligible for voting"
print(b)