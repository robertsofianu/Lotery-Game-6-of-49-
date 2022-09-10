from random import sample


x = input('Primul Numar: ')
nr_1 = int(x)

while(nr_1 > 49):
    print(f'{x} este invalid, introduceti un numar mai mic de 49!')
    x = input('Primul Numar: ')
    nr_1 = int(x)

a = input('Al doilea Numar: ')
nr_2 = int(a)

while(nr_2 > 49):
    print(f'{a} este invalid, introduceti un numar mai mic de 49!')
    a = input('Al doilea Numar: ')
    nr_2 = int(a)

while(nr_1 == nr_2):
    print(f'{nr_2} a mai fost introdus, introduceti alt numar!')
    a = input('Al doilea Numar: ')
    nr_2 = int(a)   

b = input('Al treilea Numar: ')
nr_3 = int(b)

while(nr_3 > 49):
    print(f'{b} este invalid, introduceti un numar mai mic de 49!')
    b = input('Al treilea Numar: ')
    nr_3 = int(b)

while(nr_3 == nr_1):
    print(f'{nr_3} a mai fost introdus, introduceti alt numar!')
    b = input('Al treilea Numar: ')
    nr_3 = int(b)
while(nr_3 == nr_2):
    print(f'{nr_2} a mai fost introdus, introduceti alt numar!')
    b = input('Al treilea Numar: ')
    nr_3 = int(b)

c = input('Al patrulea Numar: ')
nr_4 = int(c)

while(nr_4 > 49):
    print(f'{c} este invalid, introduceti un numar mai mic de 49!')
    c = input('Al patrulea Numar: ')
    nr_4 = int(c)

while(nr_4 == nr_1):
    print(f'{nr_1} a mai fost introdus, introduceti alt numar!')
    c = input('Al patrulea Numar: ')
    nr_4 = int(c)

while(nr_4 == nr_2):
    print(f'{nr_2} a mai fost introdus, introduceti alt numar!')
    c = input('Al patrulea Numar: ')
    nr_4 = int(c)

while(nr_4 == nr_3):
    print(f'{nr_3} a mai fost introdus, inttroduceti alt numar!')
    c = input('Al patrulea Numar: ')
    nr_4 = int(c)


d = input('Al cincilea Numar: ')
nr_5 = int(d)

while(nr_5 > 49):
    print(f'{d} este invalid, introduceti un numar mai mic de 49!')
    d = input('Al cincilea Numar: ')
    nr_5 = int(d)

while(nr_5 == nr_1):
    print(f'{nr_5} a mai fost introdus, introduceti alt numar!')
    d = input('Al cincilea Numar: ')
    nr_5 = int(d)

while(nr_5 == nr_2):
    print(f'{nr_5} a mai fost introdus, introduceti alt numar!')
    d = input('Al cincilea Numar: ')
    nr_5 = int(d)

while(nr_5 == nr_3):
    print(f'{nr_5} a mai fost introdus, introduceti alt numar!')
    d = input('Al cincilea Numar: ')
    nr_5 = int(d)

while(nr_5 == nr_4):
    print(f'{nr_5} a mai fost introdus, introduceti alt numar!')
    d = input('Al cincilea Numar: ')
    nr_5 = int(d)

e = input('Al saselea Numar: ')
nr_6 = int(e)

while(nr_6 > 49):
    print(f'{e} este invalid, introduceti un numar mai mic de 49!')
    e = input('Al saselea Numar: ')
    nr_6 = int(e)


while(nr_6 == nr_1):
    print(f'{nr_6} a mai fost introdus, introduceti alt numar!')
    e = input('Al cincilea Numar: ')
    nr_6 = int(e)

while(nr_6 == nr_2):
    print(f'{nr_6} a mai fost introdus, introduceti alt numar!')
    e = input('Al cincilea Numar: ')
    nr_6 = int(e)

while(nr_6 == nr_3):
    print(f'{nr_6} a mai fost introdus, introduceti alt numar!')
    e = input('Al cincilea Numar: ')
    nr_6 = int(e)

while(nr_6 == nr_4):
    print(f'{nr_6} a mai fost introdus, introduceti alt numar!')
    e = input('Al cincilea Numar: ')
    nr_6 = int(e)

while(nr_6 == nr_5):
    print(f'{nr_6} a mai fost introdus, introduceti alt numar!')
    e = input('Al cincilea Numar: ')
    nr_6 = int(e)

list_nr = [nr_1, nr_2, nr_3, nr_4 , nr_5, nr_6]
list_nr.sort(key = int)
print(f'Numerele tale sunt: {list_nr}')

random_nr = sorted(sample(range(1 ,49), k = 6))
print(f'Numerele catigatoare sunt: {random_nr}')



list_nr_com = list(set(list_nr).intersection(set(random_nr)))
print(list_nr_com)

if(len(list_nr_com) == 2):
    print('Ai 5 lei!')
elif(len(list_nr_com) == 3):
    print('Ai castigat 15 de lei!')
elif(len(list_nr_com) == 4):
    print('Ai castigat 500 de lei!')
elif(len(list_nr_com) == 5):
    print('Ai castigat 5000 de lei!')
elif(len(list_nr_com) == 6):
    print('Ai castigat 50000 de lei!')
else:
    print('Nu ai castigat nimic!')  