def addition(num1, num2) :
    return num1 + num2

def subtraction(num1, num2) :
    return num1 - num2

def multiplication(num1, num2) :
    return num1 * num2

def division(num1, num2) :
    return num1 / num2

def square(num1, num2) :
    return num1 ** num2


def calculation(num1, num2, op) :
    switcher = {
        '+' : addition(num1, num2),
        '-' : subtraction(num1, num2),
        '*' : multiplication(num1, num2),
        '/' : division(num1, num2),
        '^' : square(num1, num2),
    }
    return switcher[op]

while True :
    num = input('Enter the first number or type "STOP" to OFF the Calculator : ')
    if num.upper() == "STOP" :
        break
    elif num.isdigit() :
        num1 = int(num)
        operators = ['+', '-', '*', '/', '^']
        op = input("Enter the Operator ['+', '-', '*', '/', '^'] : ")
        if operators.count(op) > 0 :
            num = input('Enter the second number : ')
            if num.isdigit() :
                num2 = int(num)
                print('Answer is : ', calculation(num1, num2, op))
        else :
            print('Please select the valid operator')

    else :
        print('Please enter the valid number')