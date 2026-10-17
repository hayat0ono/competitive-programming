def func(a_len, a, x):
    ans = 1
    for _ in range(a_len):
        ans *= a
        a += x
    return ans

def main():
    n = int(input())
    for a_len in range(3, 21):
        for a in range(1, int(n ** (1/3)) + 2):
            left = 0
            right = int(n**(1/2)) + 1
            while True:
                v = func(a_len, a, (left + right) // 2)
                if v <= n:
                    left = (left + right) // 2
                elif v > n:
                    right = (left + right) // 2
                if left == right or left + 1 == right:
                    break
            if left == 0:
                break
            ans += left
    print(ans)

if __name__ == '__main__':
    main()
