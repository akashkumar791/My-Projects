num = int(input('Enter a Number'))


def FactorialValue(num):
    sums =1
    for i in range(1,num+1):
        sums = i*sums
    print('Factorial of the Number is: ',sums)
        
FactorialValue(num)