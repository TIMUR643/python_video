my_list_1 = [2, 2, 5, 12, 8, 2, 12]
print(my_list_1)
result = []
for i in my_list_1:
    if my_list_1.count(i) < 2:
        result.append(i)

print(result)
