# wap to calculate 0-50 fibonacci series
a, b=0, 1 
count = 0
print("fibonacci series :")
while count < 15:
    print(a, end=" ")
    a, b =b, a+b
    count +=1