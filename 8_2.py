def max_number():
    numbers = []
    for i in range(3):
        num = int(input("Введите число: "))
        numbers.append(num)
    return max(numbers)

print(max_number())
