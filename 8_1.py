def get_info(name, age, city):
    result = f'{name}, {age} years, lives in {city} city'
    return result

name = input('Enter name: ')

while True:
    age = int(input('Enter age: '))
    if age >= 0:
        break

city = input('Enter city: ')

print(get_info(name, age, city))
