from random import randint
n,k,l=map(int,input('Введите размер последовательности, а также её нижний и верхний предел: ').split())
def list1(n, k, l):
    return [randint(k, l) for i in range(n)]

def get(list):
    return [i for i in set(list)]
list2 = list1(n, k, l)
print(list2)
print(get(list2))