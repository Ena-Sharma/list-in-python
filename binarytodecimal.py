binary_num=[1,0,0,1,1,0,1,1]
index=len(binary_num)-1
count=0
sum=0
while index>=0:
    a=binary_num[index]*2**count
    sum=sum+a
    count=count+1
    index=index-1
print(sum)