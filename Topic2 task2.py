#Write a script that takes two numbers as input and prints whether the first number is greater than, less than, or equal to the second number.
n1=int(input("Enter 1st number:"))
n2=int(input("Enter 2nd number:"))
if n1>n2:
    print(str(n1)+" is greater than "+str(n2))
elif n1<n2:
    print(str(n1)+" is less than "+str(n2))
elif n1==n2:
    print(str(n1)+" is equal to "+str(n2))
