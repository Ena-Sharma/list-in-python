list=[1,2,3,4,5,6]
print("Initial list:")
print(list)
slicing=list[3:6]
print(slicing)
slicing_list=list[:-5]
print(slicing_list)


list.pop()
print(list)

for i in range(len(list)):
    print(i, end=" ")
print("\r")