def main():
    n = int(input())
    a = list(map(int, input().split()))

    s = [0 for _ in range(n + 1)]
    for i in range(n):
        s[i + 1] = s[i] + a[i]

    min_backwards = s.copy()
    max_backwards = s.copy()
    for i in range(n - 1, -1, -1):
        min_backwards[i] = min(min_backwards[i], min_backwards[i + 1])
        max_backwards[i] = max(max_backwards[i], max_backwards[i + 1])

    min_forwards = s.copy()
    max_forwards = s.copy()
    for i in range(n):
        min_forwards[i + 1] = min(min_forwards[i + 1], min_forwards[i])
        max_forwards[i + 1] = max(max_forwards[i + 1], max_forwards[i])

    ans = max_forwards[-1] - min_forwards[-1] + 1
    for i in range(n):
        min_val = min(min_forwards[i], min_backwards[i + 1] - 2 * a[i])
        max_val = max(max_forwards[i], max_backwards[i + 1] - 2 * a[i])
        ans = max(ans, max_val - min_val + 1)

    print(ans)

if __name__ == '__main__':
    main()
