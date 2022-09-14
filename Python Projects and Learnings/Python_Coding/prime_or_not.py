
num = int(input('Enter a value:'))
if num < 2:
    print('Not a Prime Number')
else:
    for i in range(2,num):
        if num % i == 0:
            print("Not a Prime number")
            break
    else:
        print("It's a Prime number")
        

