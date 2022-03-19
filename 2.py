from math import sqrt


def norm(vector, type):
    match type:
        case('L1'):
            res = sum((map(abs, vector)))

        case('L2'):
            res = sqrt(sum(map(lambda x: x**2, vector)))

        case('L00'):
            res = max(map(abs, vector))

        case _:
            raise TypeError(
                'Wrong argument type \navailable types: "L1" , "L2" , "L00"')
    return res


if __name__ == '__main__':
    vec = [20, -12, -50, 123]
    print(norm(vec, 'L1'))
    print(norm(vec, 'L2'))
    print(norm(vec, 'L00'))
