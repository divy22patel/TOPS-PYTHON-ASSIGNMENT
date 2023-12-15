#Write a Python program that will return true if the two given integervalues are equal or their sum or difference is 5.

a = int(input("Enter no "))
b = int(input("Enter no "))

if a==b or (a-b)==5 or (b-a)==5:
    print("true")
else:
    print("false")