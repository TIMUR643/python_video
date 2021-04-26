def get_info(name, age, city):
    result = '{name}, {age} лет, живет в {city}'
    return result

name = input('Как вас зовут?: ')

while True:
    age = int(input('Сколько вам лет?: '))
    if age >= 0:
        break

city = input('Где вы живете?: ')

print(get_info(name, age, city))
