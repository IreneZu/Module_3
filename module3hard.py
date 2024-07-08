# Задание "Раз, два, три, четыре, пять .... Это не всё?"
# __________________________________________________________

#############################################################
# Вариант 1 - преобразуем все в строку, убираем лишние знаки, суммируем

def calculate_structure_sum(data_structure):
    data__str = str(data_structure)

    a = ' '
    # убираем все символы, кроме кавычек и пробелов
    symbols = ['[', ']', '{', '}', ':', '(', ')', ',']
    for s in symbols:
        data__str = data__str.replace(s,a)

    data_list = data__str.split()
    summ = 0
    for word in data_list:
        if word.isnumeric():
            summ += int(word)
        else:
            summ += len(word.strip("'").strip('"'))

    return summ


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result1 = calculate_structure_sum(data_structure)
print(result1)

#############################################################
#  Вариант 2: - разбираем исходную структуру на подструктуры,
#  используем рекурсию

sum2 = 0

def calculate_structure_sum_2(*data_structure):
    global sum2
    for i in data_structure:
        if isinstance(i, int):
            sum2 += i
        elif isinstance(i, str):
            sum2 += len(i)
        elif isinstance(i, dict):
            calculate_structure_sum_2(i.items())
        else:
            calculate_structure_sum_2(*i)
    return


#result2 =
calculate_structure_sum_2(*data_structure)
print(sum2)

######################################################
#  Вариант 3: то же, что и вар.2, с использованием map()

def calc(data_):
    if isinstance(data_, int):
        return data_
    elif isinstance(data_, str):
        return len(data_)
    elif isinstance(data_, dict):
        return calculate_structure_sum_3(data_.items())
    else:
        return calculate_structure_sum_3(*data_)


def calculate_structure_sum_3(*data_structure):

    return sum(map(calc, data_structure))


result3 = calculate_structure_sum_3(*data_structure)
print(result3)
