# Write a Python program to find the first appearance of the substring 'not'
# and 'poor' from a given string, if 'not' follows the 'poor', replace the whole
# 'not'...'poor'substring with 'good'. Return the resulting string.

s = input("Enter String ")
s1 = s.split()

i1=s1.index("not")
i2=s1.index("poor")

if i1-i2==1 or i2-i1==1:
    s1[i1]="good"
    s1.pop(i2)

print(str(s1))


