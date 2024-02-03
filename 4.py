f = [i.split('*') for i in open('space.txt')]   #ввод


for i in range(1,len(f)):    #обход каждого корабля
    ans = (f[i][1][-3:].upper() + f[i][0][1:3][::-1].upper() + f[i][1][:3][::-1].upper())   #генерация пароля
    print(f[i][0],f[i][1],f[i][2],f[i][3],ans,sep = ';')    #вывод