f = [i.split('*') for i in open('space.txt')]   # ввод
d = {}
for i in range(1,len(f)):  # создание хэш-таблицы
    d[f[i][0]] = f[i][1]

k = 0
for i in d:  # перебор элементов таблицы
    if k == 10:  # счётчик количества выведенных элементов таблицы
        break
    k+=1
    print(f'{i}:{d[i]}')   # вывод