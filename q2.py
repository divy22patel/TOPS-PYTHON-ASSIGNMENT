#Write a Python program to get the Factorial number of given number

a = int(input("Enter a num "))
i=1
while a>0:
    i=i*a
    a-=1

print(f"Factorial = {i}")