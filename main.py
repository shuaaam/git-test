def star(n):
    for i in range(n // 2 + 1):
        for j in range(i + 1):
            print('*', end='\r')
        print()
        print()
def print_hi(name, familyname):
    result = f'Hi, {name} {familyname}'
    return result  # Press ⌘F8 to toggle the breakpoint.


def print_hi_2(name, familyname):
    res = f'Hi, {name} {familyname}'
    print(res)  # Press ⌘F8 to toggle the breakpoint.


def mappp(n):
    for i in range(n // 2 + 1):
        for j in range(i + 1):
            print('*', end='')
        print()
    for k in range(n // 2, 0, -1):
        for v in range(k):
            print('*', end='')
        print()


if __name__ == '__main__':
    mappp(9)
    print('\r')
