import random

eng_dict = {'hello': 'privet', 'bye': 'poka', 'lesson': 'urok'}


while True:
    print(random.choice(list(eng_dict.keys())))
    user_answer = input('Please enter word translation:  ')
    if user_answer.lower() in 'exit':
        break
    elif user_answer.lower() in 'show':
        print(eng_dict)
    elif user_answer.lower() not in eng_dict.values():
        print('Wrong answer')
    elif user_answer.lower() in eng_dict.values():
        continue
