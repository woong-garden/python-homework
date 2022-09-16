score = int(input())

def get_grade(score):
    if 90 < score <= 100:
        return('A')
    elif 80 < score <= 90:
        return ('B')
    elif 70 < score <= 80:
        return ('C')
    else:
        return ('F')

grade = get_grade(score)
print(grade)