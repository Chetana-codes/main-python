#WAP to print a multiplication table of a given number
n = int(input("enter the number"))
for i in range(1,11):
    print(n,"x",i,"=",(n*i))
print("multiplication table is", n)    
