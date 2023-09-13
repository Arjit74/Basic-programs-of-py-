# WAP that calculates the given number of seconds into hours ,minutes,and seconds.
a=int(input("Enter the seconds to be converted:- "))
b= a//60
c= b//60
print("the no. of hours is :-",b)
print("the no. of minutes is :- ",c)
print("the no. of seconds is :-",a%60)