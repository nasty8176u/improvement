from random import randint
import itertools
n,m=map(int,input('Введите нижний и верхний предел, из которого будет взят коэффициент k: ').split())
k = randint(n, m)

def get_numbers(k):
    numbers = [randint(0, 10) for i in range (k + 1)]
    while numbers[0] == 0:
        numbers[0] = randint(1, 10) 
    return numbers

def get_pol(k, numbers):
    var = ['*x^']*(k-1) + ['*x']
    pol = [[a, b, c] for a, b, c  in itertools.zip_longest(numbers, var, range(k, 1, -1), fillvalue = '') if a !=0]
    for x in pol:
        x.append(' + ')
    pol = list(itertools.chain(*pol))
    pol[-1] = ' = 0'
    return "".join(map(str, pol)).replace(' 1*x',' x')

numbers = get_numbers(k)
polynom1 = get_pol(k, numbers)
print('Итоговый результат равен', polynom1)

l=int(input('Введите нижний предел, из которого будет взят коэффициент k: '))
p=int(input('Введите верхний предел, из которого будет взят коэффициент k: '))
k = randint(l, p)

numbers = get_numbers(k) 
polynom2 = get_pol(k, numbers)
print(polynom2)

with open('33_Polynomial2.txt', 'w') as data:
    data.write(polynom2)