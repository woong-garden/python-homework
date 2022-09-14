while True:
    try:
        a, b = map(int,input().split())
        break
    except:
        print('숫자만 입력해주세요')
        
class Calc:
    
    def set_number(self,first,second):
        self.first = first
        self.second = second
    def plus(self):
        result = self.first + self.second
        return result
    def minus(self):
        result = self.first - self.second
        return result
    def multiple(self):
        result = self.first * self.second
        return result
    def divide(self):
        try:
            result = self.first / self.second
            
            return result
        except:
            result = '0으로는 나눌 수 없습니다!'
            return result


calc = Calc()
calc.set_number(a,b)
print(calc.plus())
print(calc.minus()) 
print(calc.multiple()) 
print(calc.divide())