#Write a Python program to count the occurrences of each word in a given sentence
t = input("Enter String ")

c1=t.split(" ")
c2=t.split(" ")

for i in range(len(c1)):
    x=1
    for j in range(i+1,len(c1)):
        if c1[i]==c2[j]:
            x+=1
            print(f"{c1[i]} {x}")




