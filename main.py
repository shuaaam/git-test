<<<<<<< HEAD
def adding(a, b):
    return a/b
=======
def star(n):
    for i in range(n // 2 + 1):
        for j in range(i + 1):
            print('*', end='\r')
        print()
        print()


def print_hi(name, familyname, optional=0):
    result = f'Hi, {name} {familyname}'
    return optional  # Press ⌘F8 to toggle the breakpoint.


def mappp(n):
    for i in range(n // 2 + 1):
        for j in range(i + 1):
            print('*', end='')
    for k in range(n // 2, 0, -1):
        for v in range(k):
            print('*', end='')
        print()
>>>>>>> 07ef82be7654455b5de4f99225f8d51508cf735f


if __name__ == '__main__':

    print(adding(10, 5))
