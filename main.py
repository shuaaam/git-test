def sun(n):
    for i in range(n // 2 + 1):
        for j in range(i + 1):
            print('*', end='\r')
        print()
        print()
def print_hi(name, familyname):
    res = f'Hi, {name} {familyname}'
    print(res)  # Press ⌘F8 to toggle the breakpoint.


def print_hi_2(name, familyname):
    print(res)  # Press ⌘F8 to toggle the breakpoint.


# def star(n):
#     for i in range(n // 2 + 1):
#         for j in range(i + 1):
#             print('*', end='')
#         print()
#     for k in range(n // 2, 0, -1):
#         for v in range(k):
#             print('*', end='')
#         print()


# Press the green button in the gutter to run the script.

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    star(9)
    print('\n')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
