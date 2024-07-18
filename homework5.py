immutable_var = 1, 2, 3,'дождь'
print(immutable_var)
#immutable_var[3] = 'снег' # Кортеж содержит не изменяемые элементы (числа и строки) поэтому его нельзя изменить
mutable_list = [1, 2, 3,'дождь']
mutable_list[3] = 'снег'
mutable_list.append('уже скоро')
print(mutable_list)