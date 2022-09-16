from pprint import pprint


users = [
    {"name": "Ronald", "age": 30, "math_score": 93, "science_score": 65, "english_score": 93, "social_score": 92},
    {"name": "Amelia", "age": 24, "math_score": 88, "science_score": 52, "english_score": 78, "social_score": 91},
    {"name": "Nathaniel", "age": 28, "math_score": 48, "science_score": 40, "english_score": 49, "social_score": 91},
    {"name": "Sally", "age": 29, "math_score": 100, "science_score": 69, "english_score": 67, "social_score": 82},
    {"name": "Alexander", "age": 30, "math_score": 69, "science_score": 52, "english_score": 98, "social_score": 44},
    {"name": "Madge", "age": 22, "math_score": 52, "science_score": 63, "english_score": 54, "social_score": 47},
    {"name": "Trevor", "age": 23, "math_score": 89, "science_score": 88, "english_score": 69, "social_score": 93},
    {"name": "Andre", "age": 23, "math_score": 50, "science_score": 56, "english_score": 99, "social_score": 54},
    {"name": "Rodney", "age": 16, "math_score": 66, "science_score": 55, "english_score": 58, "social_score": 43},
    {"name": "Raymond", "age": 26, "math_score": 49, "science_score": 55, "english_score": 95, "social_score": 82},
    {"name": "Scott", "age": 15, "math_score": 85, "science_score": 92, "english_score": 56, "social_score": 85},
    {"name": "Jeanette", "age": 28, "math_score": 48, "science_score": 65, "english_score": 77, "social_score": 94},
    {"name": "Sallie", "age": 25, "math_score": 42, "science_score": 72, "english_score": 95, "social_score": 44},
    {"name": "Richard", "age": 21, "math_score": 71, "science_score": 95, "english_score": 61, "social_score": 59},
    {"name": "Callie", "age": 15, "math_score": 98, "science_score": 50, "english_score": 100, "social_score": 74},
]

def get_filter_user(users):
    filter_users = []  #리스트로 담아주는 곳!
    
    for user in users:     #반복문으로 users에서 하나씩 돌면서 user로 넣어줌
        total_score = user['math_score'] + user['science_score'] + user['english_score'] + user['social_score'] 
                        #넣어둔 user에서 score들을 가져와서 합한다.
        average_score = total_score / 4 #평균을 구하기위해서 4로 나눔

        user_dic = {}   #새로 담아줄 딕셔너리를 만듦
        if average_score >= 70: #평균이 70점 이상일때 조건문 설정
            user_dic['name'] = user['name'] #user['name']에 값을 새로운 user_dic['name']에 키값으로 설정
            user_dic['age'] = user['age']   #user['age']에 값을 새로운 user_dic['age']에 키값으로 설정
            filter_users.append(user_dic)   #filter_users에 새로만든 user_dic을 담아준다.  
                    
    return filter_users

filter_users = get_filter_user(users)
pprint(filter_users)
