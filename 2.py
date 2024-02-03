f = [i.split('*')[0] for i in open('space.txt')] #ввод

for i in range(1,len(f)):
    for j in range(1,len(f)):
        if int(f[i][5:])<int(f[j][5:]):  #сортировка
            f[i],f[j] = f[j],f[i]

for i in range(1,11):   #вывод
    print(f[i])