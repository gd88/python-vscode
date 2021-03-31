def problemDescription():
    print('* Number of divisors *')

def getNumOfDivisors(number):
    a=0
    for i in range(1,number+1):
        if number%i == 0:
            a=a+1
    return a


problemDescription()
print('Type the first number:')
b=int(input())
print('Type the second number: ')
c=int(input())
num1 = getNumOfDivisors(b)
num2 = getNumOfDivisors(c)
print('Number of divisors of the first number is ' + str(num1))
print('Number of divisors of the second number is ' + str(num2))
