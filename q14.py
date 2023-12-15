#Write a Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string

a = input("Enter String 1 ")
b = input("Enter String 2 ")
c = (a+" "+b)
d=c.split()

for i in range(len(d)):
    temp=d[i]
    d[i]=temp[1]+temp[0]+temp[2:]

print(d)

