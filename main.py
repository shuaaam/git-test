def star(n):
    for i in range(n // 2 + 1):
        for j in range(i + 1):
            print('*', end='')
        print()
    for k in range(n // 2, 0, -1):
        for v in range(k):
            print('*', end='')
        print()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    star(9)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
