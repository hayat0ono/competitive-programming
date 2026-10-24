def solve(s, id_dict, id_now):
    if s in id_dict:
        print(id_dict[s])
    else:
        id_dict[s] = id_now
        print(id_now)
        id_now += 1
    return id_dict, id_now

def main():
    q = int(input())
    id_dict = {}
    id_now = 1
    for _ in range(q):
        s = input()
        id_dict, id_now = solve(s, id_dict, id_now)

if __name__ == '__main__':
    main()
