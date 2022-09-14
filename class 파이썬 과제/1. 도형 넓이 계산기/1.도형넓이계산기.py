
# 1. 클래스만들기
#2. 인스턴스를 선언하기 


class Shape:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def square(self):
        result = self.width * self.height
        return result
    def triangle(self):
        result = self.width * self.height / 2
        return result
    def circle(self):
        result = (self.width/2) ** 2 * 3.14
        return result


figure_width_height = Shape(10, 10) 
print(figure_width_height.square())
print(figure_width_height.triangle())
print(figure_width_height.circle())