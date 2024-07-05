# Счётчик вызовов
calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()
    return string.lower() in ' '.join(list_to_search).lower().split()

# Интерактивный ввод исходных данных

n = int(input('Сколько раз повторять ввод ?: '))
strings = []
str_and_lists = []

def num_str(num, input_num):  # добавляем порядковый номер ввода
    my_str = ''
    if n > 1:
        my_str = str(i + 1) + '-ю '
    return my_str

for i in range(n):
     strings.append(input('Введите '+ num_str(n, i) + 'строку : '))
for i in range(n):
    str_and_lists.append((input('Введите '  + num_str(n, i) + 'искомую строку: '),
                          input('Введите список для поиска искомой строки (слова с пробелами): ').split()))

for i in range(n):
    print(string_info(strings[i]))
for i in range(n):
    print(is_contains(str_and_lists[i][0], str_and_lists[i][1]))

print(calls)
