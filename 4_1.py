my_list_1 = [2, 5, 8, 2, 12, 12, 4]
my_list_2 = [2, 7, 12, 3]
print(my_list_1)
print(my_list_2)

my_list_1 = list(set(my_list_1))
for x in my_list_1:
    for y in my_list_2:
        if x == y:
            my_list_1.remove(x)




print(my_list_1)
