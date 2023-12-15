#Write a Python program to count occurrences of a substring in a string

a = input("Enter String ")
b = input("Enter SubString ")
x=0
for i in range(len(a)-1):
    if b==a[i:i+len(b)]:
        x+=1

print("Number of Occurrence ",x)