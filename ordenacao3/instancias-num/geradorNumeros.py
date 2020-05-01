import random as r

arquivo = open('5digitos-1.in', 'w')
for i in range(1000):
    arquivo.write(str(r.randint(10000,99999))+'\n')