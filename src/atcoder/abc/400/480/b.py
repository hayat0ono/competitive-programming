def correct(s, t):
    count = 0
    if len(s) != len(t):
        return -1
    for i in range(len(s)):
        if s[i] == t[i] and s[i] != '?' and t[i] != '?':
            count += 1
    if count == len(s):
        return 0
    if count >= len(s) - 1:
        return 1
    return -1

def main():
    n, m = map(int, input().split())
    subjects = []
    d = {}
    for i in range(n):
        s = input()
        subjects.append(s)
        d[s] = 0
    for i in range(m):
        correct_subjects_perf = []
        correct_subjects = []
        t = input()
        for s in subjects:
            res = correct(s, t)
            if res == 0:
                correct_subjects_perf.append(s)
            elif res == 1:
                correct_subjects.append(s)
        if len(correct_subjects_perf) == 1:
            d[correct_subjects_perf[0]] += 1
            continue
        if len(correct_subjects) == 1:
            d[correct_subjects[0]] += 1
    for s in subjects:
        print(d[s])

if __name__ == '__main__':
    main()
