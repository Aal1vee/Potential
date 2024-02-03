f = [i.split('*') for i in open('space.txt')]   #ввод
f1 = open('space_new.txt','w')

for i in range(1,len(f)):
    n = int(f[i][0][5])
    m = int(f[i][0][6])
    xd = int(f[i][3].split()[0])
    yd = int(f[i][3].split()[1])
    t = len(f[i][1])
    if n>5:
        x = n+xd         #   Определение координаты Х
    else:
        x = -1*(n+xd)*4+t

    if m>3:
        y = m+t+yd         #   Определение координаты Y
    else:
        y = -1*(n+yd)*m
    ans = f"{f[i][0]} - ({x},{y})"
    #print(ans)
    f1.write(ans+'\n')      #    Вывод
    if f[i][0][3] == 'V':
        print(f[i][0])
f1.close()