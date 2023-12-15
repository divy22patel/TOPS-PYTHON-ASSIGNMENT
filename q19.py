# Write a Python function to insert a string in the middle of a string

def stringInsert(s1,s2,pos):
    lst = s1.split()
    lst.insert((pos-1),s2)
    s=""
    for i in lst:
        s+=(i+" ")
    print(s)

stringInsert("divy patel","c",2)