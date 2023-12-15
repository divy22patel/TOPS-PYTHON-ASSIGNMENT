#Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

a = int(input("Enter NO "))
b = int(input("Enter NO "))
c = int(input("Enter NO "))

if a==b or b==c or c==a:
    print(f"Sum is {0}")
else:
    print(f"Sum {a+b+c}")