#wap to to calculate the sum  of all the odd numbers within the given range 
given_range = int(input("enter the 0 to given range "))
sum = 0 
for i in range(given_range):
    if i%2!=0:
        sum+=i 
print(sum)

