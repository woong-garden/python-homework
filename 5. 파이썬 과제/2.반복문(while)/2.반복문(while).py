


def my_function():
    count = 1
    while count <=5 :  
        number = input('숫자를 입력하세요! 입력취소는 exit 입력 :')
        try:          
            if number == 'exit':
                break
            if type(int(number)) == int:
                print(int(number)*2)
                print('두번째',count)
                count += 1
        except:
            print(f'입력한 문자는 {number}입니다.')
        
my_function()




