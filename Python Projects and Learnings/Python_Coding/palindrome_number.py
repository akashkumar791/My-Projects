
num = int(input('Enter Number' ))

def PalindromeCheck(num):
    x1=str(num)[::-1]
    if str(num) == x1:
        print("It's a palindrome number")
    else:
        print("It's Not a palindrome number")
            
PalindromeCheck(num)    
    