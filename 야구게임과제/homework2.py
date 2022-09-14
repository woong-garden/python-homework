from random import randint
import time
from datetime import datetime, timedelta



choice_numbers = int(input("몇 자리 숫자인지 입력하세요~! : "))
    
start_time = time.time()




def generate_numbers():
    
    numbers = []

    while len(numbers) < choice_numbers:
        num = randint(0,9)
        if num not in numbers:
            numbers.append(num)

    print(f"0과 9 사이의 서로 다른 숫자 {choice_numbers}개를 랜덤한 순서로 뽑으세요!")
    
    print(numbers)
    return numbers





def take_guess():

    print(f"숫자 {choice_numbers}개를 하나씩 차례대로 입력하세요")

    new_guess = []
    while len(new_guess) < choice_numbers:
        new_num = input("{}번째 숫자를 입력하세요. 종료하고 싶으시면 exit 입력하세요: ".format(len(new_guess)+1))
        
        
        if new_num == "exit":
            return 'exit'

        new_num = int(new_num)    

        if new_num < 0 or new_num > 9:
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요")
        elif new_num in new_guess:
            print('중복되는 숫자입니다. 다시입력하세요')
        else:
            new_guess.append(new_num)
    
    return new_guess






def get_score(guess, solution):
    strike_count = 0
    ball_count = 0

    for i in range(choice_numbers):
        if guess[i] == solution[i]:
            strike_count += 1
        elif guess[i] in solution:
            ball_count += 1

    return strike_count, ball_count





answer = generate_numbers()
tries = 0

while True:
    user_guess = take_guess()
    if user_guess == 'exit':
        break
    s, b = get_score(user_guess, answer)

    print('{}s {}b'.format(s,b))
    tries += 1

    if s == choice_numbers:
        end_time=time.time()
        print(f"축하합니다. {tries}번 만에 {choice_numbers}자리 숫자의 값과 위치를 모두 맞췃습니다.")
        print(f'소요시간 : {end_time-start_time:.0f} 초')
        now = datetime.now()
        print('맞춘 시점 날짜/시간 : ',now.strftime('%Y년 %m월 %d일 %H시 %M분 %S초'))
        break
        
    