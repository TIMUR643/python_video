import random

main_number = int(input('Загадай число (от 1 до 100):'))
comp_number = 0
max_number = 100;
min_number = 1;

comp_number = random.randint(min_number, max_number)
while main_number != comp_number:
    print("Это ваше число?", comp_number)
    main_decision = input("Вы загадали больше/меньше? (Введите '>' или '<')")
    if main_decision == ">":
            min_number = comp_number + 1
            comp_number = random.randint(min_number, max_number)
    elif main_decision == "<":
            max_number = comp_number - 1
            comp_number = random.randint(min_number, max_number)
    elif main_decision == "=":
            comp_number = main_number
else:
    print("Ваше число: ", comp_number,'   Угадал!')
