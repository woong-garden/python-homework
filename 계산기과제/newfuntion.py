
#case 1
def clr(num1, num2, num3):
    if num2 == '+':
        print(f'{num1} + {num3} = {num1 + num3}')   
    elif num2 == '-':
        print(f'{num1} - {num3} = {num1 - num3}')      
    elif num2 == '*':
        print(f'{num1} * {num3} = {num1 * num3}')
    elif num2 == '/':
        if num3 == 0:
            print("0으로 나눌 수 없습니다!")
        else:
            print(f'{num1} / {num3} = {num1 / num3}')






# #case 2
# def add(a, c):    
#     return a + c

# def subtract(a, c):
#     return a - c

# def multiply(a, c):
#     return a * c

# def div(a, c):
#     return a / c
