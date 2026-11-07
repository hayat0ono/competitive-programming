def main():
    n, m = map(int, input().split())
    votes = {}
    for i in range(1, n+1):
        votes[i] = {'first': 0, 'second': {}}
    for _ in range(m):
        a, b = map(int, input().split())
        votes[a]['first'] += 1
        if b not in votes[a]['second']:
            votes[a]['second'][b] = 0
        votes[a]['second'][b] += 1
    ans_init = 0

    ans_init = max(votes, key=lambda k: (votes[k]['first'], -k))

    for i in range(1, n+1):
        if i == ans_init:
            votes_cp = {k: votes[k]['first'] for k in votes if k != i}
            for k, v in votes[i]['second'].items():
                votes_cp[k] += v
            ans = max(votes_cp, key=lambda k: (votes_cp[k], -k))

        else:
            ans = ans_init
            vote_max = votes[ans]['first']
            if ans in votes[i]['second']:
                vote_max += votes[i]['second'][ans]
            for k, v in votes[i]['second'].items():
                if k == ans_init:
                    continue
                if votes[k]['first'] + v > vote_max:
                    ans = k
                    vote_max = votes[k]['first'] + v
                elif votes[k]['first'] + v == vote_max:
                    ans = min(ans, k)
        print(ans)

if __name__ == '__main__':
    main()
