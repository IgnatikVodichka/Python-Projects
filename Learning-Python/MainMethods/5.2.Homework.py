import random

eng_dict = {
    'hello':  'privet',
    'bye':    'poka',
    'lesson': 'urok',
}

keys = list(eng_dict.keys())

while True:
    word = random.choice(keys)
    correct_answer = eng_dict[word]
    print(word)

    user_answer = input('Please enter word translation: ').lower()
    if user_answer == 'exit':
        break
    elif user_answer == 'show':
        print(eng_dict)
    elif user_answer != correct_answer:
        print('Wrong answer')
