# Write a Python function to reverses a string if its length is a multiple of 4

a = input("Enter A String ")
lst = a.split()

for i in range(len(lst)):

    if len(lst[i])%4==0:
        lst[i]=lst[i][::-1]

for i in lst:
    print(i+" ",end="")


