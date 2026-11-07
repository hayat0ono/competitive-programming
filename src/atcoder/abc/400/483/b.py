def main():
    n, q = map(int, input().split())
    k = list(map(int, input().split()))
    ans = [i for i in range(1, n+1)]
    for i in range(q):
        if k[i] == n:
            ans = [-x for x in ans[::-1]]
        else:
            ans = [-x for x in ans[:k[i]][::-1]] + ans[k[i]:]
    for i in range(n):
        print(ans[i])

if __name__ == '__main__':
    main()
