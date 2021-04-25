print('Игра "Загадай число от 0 до 100"')

user_number = int(input('Введите число'))
try_comp_number = None

user_higher = ">"
user_lower = "<"
user_answer = None

import random
min = 1
max = 100

while user_number != try_comp_number:
    try_comp_number = int(random.randint(min, max))
if try_comp_number == user_number:
    print('Компьютер догадался. Ваше число: ', try_comp_number)
else:
    print('Ваше число больше или меньше: ', try_comp_number, '? (используйте клавиши > или <)')
user_answer = input()
if user_answer == user_lower:
    max = try_comp_number
elif user_answer == user_higher:
    min = try_comp_number
