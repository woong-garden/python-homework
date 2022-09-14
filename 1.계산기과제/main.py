from newfuntion import clr


# #case1
print("이항식 사칙연산만 할 수 있는 계산기 입니다!")
a = int(input("첫번째 값을 입력하세요 : "))  
b = input("사칙연산을 넣으세요( +, -, * , / ):")
c = int(input("두번째 값을 입력하세요 : ")) 

num1 = a
num3 = c
if b not in ['+', '-', '*' , '/']:
    print("사칙연산을 잘못입력했습니다!")
else:
    num2 = b

clr(num1, num2, num3)




#case 2
# print("이항식 사칙연산만 할 수 있는 계산기 입니다!")
# a = int(input("첫번째 값을 입력하세요 : "))  
# b = input("사칙연산을 넣으세요( +, -, * , / ):")
# if b not in ['+', '-', '*' , '/']:
#     print("잘못입력했습니다.")
    
# c = int(input("두번째 값을 입력하세요 : "))

# answer = ''

# if b() == '+':
#     answer = newfuntion.add(a, c)
#     print(answer)
# elif b == '-':
#     answer = newfuntion.subtract(a,c)
#     print(answer)
# elif b == '*':
#     answer = newfuntion.multiply(a,c)
#     print(answer)
# elif b == '/':
#     if c == 0:
#         print("0으로 나눌수없습니다!")
#     else:
#         answer = newfuntion.div(a,c)
#         print(answer) 
    
