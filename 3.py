f = [i.split('*') for i in open('space.txt')]   #ввод
a = [i[0] for i in f]    # массив планет
x = input()    # ввод
while x!='stop': # постоянный запуск программы
    if x in a:    # проверка на наличие корабля
        ind = a.index(x)
        print(f'Корабль {f[ind][0]} был отправлен с планеты: {f[ind][1]} и его направление движения было: {f[ind][3]}')  # вывод
    else:
        print('error.. er.. ror..')    # вывод
    x = input()