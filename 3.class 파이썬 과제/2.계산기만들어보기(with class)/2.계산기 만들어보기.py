class Calc:
    # def __init__(self,first,second):
    #     self.first = first
    #     self.second = second
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
        result = self.first / self.second
        return result


calc = Calc()
calc.set_number(20,10)
print(calc.plus())
print(calc.minus()) 
print(calc.multiple()) 
print(calc.divide())