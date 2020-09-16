List = [] 
print("Initial blank List: ") 
print(List) 



for i in range(1, 4): 
    List.append(i) 
print("\nList after Addition of elements from 1-3: ") 
print(List) 
List.append((5, 6)) 
print("\nList after Addition of a Tuple: ") 
print(List) 
List2 = ['For', 'Geeks'] 
List.append(List2) 
print("\nList after Addition of a List: ") 
print(List) 


List.insert(3, 12) 
List.insert(0, 'Geeks') 
print("\nList after performing Insert Operation: ") 
print(List) 


List.extend([8, 'rumour', 'Always']) 
print("\nList after performing Extend Operation: ") 
print(List) 


List.extend(['Manisha','abcs'])
print(List)

List.pop()
print(List)
