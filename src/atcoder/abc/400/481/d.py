import heapq

def main():
    n, m, s, t = map(int,input().split())
    s -= 1
    t -= 1
    path_dict = {}
    for i in range(n):
        path_dict[i] = {'nxt': [], 'min': float('inf')}
    for _ in range(m):
        a, b = map(int,input().split())
        a -= 1
        b -= 1
        path_dict[a]['nxt'].append(b)
        path_dict[a]['min'] = min(path_dict[a]['min'], b)
    pq = []
    costs = [float('inf') for _ in range(n)]
    costs[s] = 0
    heapq.heappush(pq, (0, s))
    while pq:
        now_tupple = heapq.heappop(pq)
        cost = now_tupple[0]
        now = now_tupple[1]
        for x in path_dict[now]['nxt']:
            if x == path_dict[now]['min']:
                if costs[x] > cost:
                    costs[x] = cost
                    heapq.heappush(pq, (costs[now], x))
            else:
                if costs[x] > cost + 1:
                    costs[x] = cost + 1
                    heapq.heappush(pq, (cost + 1, x))
    if costs[t] == float('inf'):
        print(-1)
    else:
        print(costs[t])

if __name__ == '__main__':
    main()
