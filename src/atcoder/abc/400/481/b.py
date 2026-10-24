def main():
    n, k = map(int,input().split())
    a = list(map(int,input().split()))
    ans = 0
    now = a[0]
    if now == k:
        ans += 1
    for i in range(1, n):
        if now < k and a[i] >= k:
            ans += 1
        elif now > k and a[i] <= k:
            ans += 1
        now = a[i]
    print(ans)

if __name__ == '__main__':
    main()
