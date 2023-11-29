# my_list = [2,2,2,2,2]
# multiplicacion = 1
# for i in my_list:
#     multiplicacion = multiplicacion * i
# print(multiplicacion)


from functools import reduce


my_list = [2,2,2,2,2]

all_multiplied = reduce(lambda a, b: a * b, my_list)
print(all_multiplied)