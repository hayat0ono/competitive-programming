import bisect

def prepare(n, a):
    p = []
    b = []
    for i in range(n):
        p.append((i+1) + (p[i-1] if i > 0 else 0))
        b.append(a[i] + (b[i-1] if i > 0 else 0))
    c = []
    for i in range(n):
        c.append(b[i] + (c[i-1] if i > 0 else 0))
    return p, b, c

def sum_to_k(p, b, c, k):
    if k == 0:
        return 0
    insert_index = bisect.bisect_right(p, k)
    if insert_index == len(p):
        return c[-1]
    elif p[insert_index - 1] == k:
        return c[insert_index - 1]
    else:
        return c[insert_index - 1] + b[k - p[insert_index - 1] - 1]

def solve(p, b, c, l, r):
    ans = sum_to_k(p, b, c, r) - sum_to_k(p, b, c, l - 1)
    print(ans)

def main():
    n, q = map(int, input().split())
    a = list(map(int, input().split()))
    p, b, c = prepare(n, a)
    for _ in range(q):
        l, r = map(int, input().split())
        solve(p, b, c, l, r)

if __name__ == '__main__':
    main()
