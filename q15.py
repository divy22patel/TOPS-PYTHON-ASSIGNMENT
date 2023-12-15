# Write a Python program to add 'ing' at the end of a given string (length
# should be at least 3). If the given string already ends with 'ing' then add
# 'ly' instead if the string length of the given string is less than 3, leave it
# unchanged.

a = input("Enter a sentence ")
a_lst = a.split()

for i in range(len(a_lst)):

    if len(a_lst[i])>=3 and a_lst[i].endswith("ing")==False:
        a_lst[i]=a_lst[i]+"ing"

    elif a_lst[i].endswith("ing"):
        a_lst[i]=a_lst[i]+"ly"



print(a_lst)


