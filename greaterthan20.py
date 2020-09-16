numbers=[50, 40, 23, 70,30,35,56, 12, 5, 10, 7]
i=0
count=0
sum=0
while i<len(numbers):
    if numbers[i]>20 and numbers[i]<40:
        
        count=count+1
        sum=sum+numbers[i]
    i=i+1
print(count,"=count ",sum,"=total")

