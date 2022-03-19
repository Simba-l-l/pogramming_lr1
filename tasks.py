from math import sin, cos
from pickle import dump, load


def task1(a):
    """function returns True if argument is integer, otherwise False"""
    return type(a) == int


def task2(list, display=False):
    res = []
    temp = [[sin(i[1][1]), i[0]] for i in enumerate(list)]
    temp.sort()
    res.append([list[i[1]] for i in temp])
    temp = [[i[1][1] + cos(i[1][0]), i[0]] for i in enumerate(list)]
    temp.sort(reverse=True)
    res.append([list[i[1]] for i in temp])
    temp = [[sin([1][0]) + cos(len(i[1][2])), i[0]] for i in enumerate(list)]
    temp.sort()
    res.append([list[i[1]] for i in temp])
    if display:
        print('\nПо синусу второго элемента, по возрастанию:')
        for i in res[0]:
            print(i)
        print('\nПо сумме второго и косинуса первого элемента, по убыванию:')
        for i in res[1]:
            print(i)
        print('\nПо сумме синуса первого элемента и косинуса длины строки, по возрастанию:')
        for i in res[2]:
            print(i)
    return res


def task3():
    text = [[[i for i in range(10)] for j in range(10)] for k in range(10)]
    with open('text.txt', 'w') as f:
        f.write(str(text))
        f.close()
    with open('bin', 'wb') as b:
        dump(text, b)
        b.close
    with open('text.txt', 'r') as f:
        print('From txt\n', type(f.read()))
    with open('bin', 'rb') as b:
        bin = load(b)
        print('From bin\n',type(bin) )
        print(bin[0][0])


if __name__ == '__main__':
    list = [(14, 0.48, 'iczjypun'),
            (13, 0.06, 'leonbpu'),
            (7, 0.0, 'inflo'),
            (1, 0.58, 'tukw'),
            (15, 0.94, 'hepgtz'),
            (4, 0.35, 'rfwzdtu'),
            (16, 0.28, 'vukow'),
            (19, 0.94, 'uxf'),
            (10, 0.88, 'kjydu'),
            (6, 0.61, 'uishdymr'),
            (5, 0.55, 'amxylfrw'),
            (11, 0.11, 'fanw'),
            (1, 0.02, 'yerpnsfhw'),
            (4, 0.18, 'xdoaq'),
            (15, 0.06, 'hpzey')]
    # task2(list, display=True)
    task3()
    
    
