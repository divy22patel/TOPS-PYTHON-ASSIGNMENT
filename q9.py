#Write a python program to sum of the first n positive integers

a = int(input("Enter Range "))
s=0
while a>0:
    s=s+a
    a-=1
print(f"Sum is {s}")
