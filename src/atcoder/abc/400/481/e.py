from fractions import Fraction

def solve(n, stars):
    slopes = []
    slopes_pos = []
    for i in range(n):
        star = stars[i]
        if star[0] == 0:
            slope = float('inf')
            if star[1] > 0:
                slopes_pos.append(slope)
            slopes.append(slope)
        elif star[0] > 0:
            slope = Fraction(star[1], star[0])
            slopes.append(slope)
            slopes_pos.append(slope)
        else:
            slope = Fraction(star[1], star[0])
            slopes.append(slope)
    slopes = sorted(slopes)
    slopes_pos = sorted(slopes_pos)
    now_pos = 0
    ans_pos = len(slopes_pos)
    ans_neg = n - ans_pos
    ans = max(ans_pos, ans_neg)
    for slope in slopes:
        if slope == float('inf'):
            break
        if now_pos < len(slopes_pos):
            if slope == slopes_pos[now_pos]:
                ans_pos -= 1
                ans_neg += 1
                now_pos += 1
            else:
                ans_pos += 1
                ans_neg -= 1
        else:
            ans_pos += 1
            ans_neg -= 1
        ans = max(ans, ans_pos, ans_neg)
    print(ans)

def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        stars = []
        for _ in range(n):
            x, y = map(int,input().split())
            stars.append([x, y])
        solve(n, stars)

if __name__ == '__main__':
    main()
