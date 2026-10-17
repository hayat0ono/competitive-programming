def main():
    x, y = list(input())
    z, w = list(input())

    if x == 'A':
        if y == 'D' or z == 'D':
            print('Yes')
            return
    if y == 'A':
        if x == 'D' or w == 'D':
            print('Yes')
            return
    if z == 'A':
        if x == 'D' or w == 'D':
            print('Yes')
            return
    if w == 'A':
        if y == 'D' or z == 'D':
            print('Yes')
            return
    print('No')
    return

if __name__ == '__main__':
    main()
