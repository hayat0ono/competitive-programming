import math

def main():
    n, k, t = map(int, input().split())
    a = list(map(int, input().split()))
    a = sorted(a)
    now = 0
    ans = 0
    for i in range(n):
        nxt = a[i]
        if nxt < t:
            if nxt > now:
                ans += math.ceil((nxt - now) / k)
            now = nxt + k
        if now >= t:
            break
    if now < t:
        ans += math.ceil((t - now) / k)
    print(ans)

if __name__ == '__main__':
    main()
