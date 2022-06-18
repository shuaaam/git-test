def star(n):
    for i in range(n // 2 + 1):
        for j in range(i + 1):
            print('*', end='\r')
        print()
        print()


# Press the green button in the gutter to run the script.
def main():
    print_hi('John', 'Smith')
    print_hi_2('John', 'Smith')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    star(9)
    print('\n')
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
