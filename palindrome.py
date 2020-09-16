a=input('enter name or no.')
b=''
i=len(a)-1
while i>=0:
    b=b+a[i]
    print(b)
    i=i-1
if b==a:
    print('it is palindrome')
else:
    print('it is not palindrome')