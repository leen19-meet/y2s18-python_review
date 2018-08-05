# Write your solution for 1.1 here!
sum=0
for i in range(101):
    sum = sum + i
print(sum) 

sum1 = 0
for i in range(101):
    if i % 2 ==0:
        sum1 = sum1 + i
print(sum1)

for i in range(1000,0,-1):
    if i%6 == 2 and i**3%5 == 3:
        print (i)
        break