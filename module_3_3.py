# Распаковка

# 1.Функция с параметрами по умолчанию:
def print_params(a = 1, b = '2', c = True):
    print(a, b, c)

print_params(2, 3, 4)
print_params(2)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])

# 2.Распаковка параметров:

values_list = [None, 1.0, 'str']
values_dict = {'a':'1', 'b':2, 'c':False}

print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:

values_list2 = ['str', 1.0]
print_params(*values_list2, 42)  # работает



