#Write a Python program to get the Fibonacci series of given range

n = int(input("Enter Range "))
a=0
b=1

print("Fibonacci ",a ,b,end=" ")
for i in range(n):
    c=a+b
    a=b
    b=c
    print(c,end=" ")

