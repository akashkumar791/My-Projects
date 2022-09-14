a = int(input('Enter the First Number'))
b = int(input('Enter the Second Number'))
n = input(int('Enter the Number of Elements'))

print(a, b, end=" ")
while n-2:
    c = a+b
    a = b
    b = c
    print(c, end =" ")
    n = n-1
