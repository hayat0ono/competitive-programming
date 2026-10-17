import random
import time

def input_all():
    n, m, k, t = map(int, input().split())
    s = list(map(int, input().split()))
    goals = [list(map(int, input().split())) for _ in range(m)]
    return n, m, k, t, s, goals

def output_all(circles, move):
    output_path = 'output.txt'
    with open(output_path, 'w') as f:
        for circle in circles:
            f.write(f'{circle[0]} {circle[1]}\n')
        for m in move:
            f.write(f'{m}\n')

    # for i in range(len(circles)):
    #     print(*circles[i])
    # for i in range(len(move)):
    #     print(move[i])
    return

def one_step(n, k, now, goal, circles, move):
    queue = []
    queue.append((now, circles, move))

    while True:
        now, circles, move = queue.pop(0)
        if now == goal:
            break
        dist_goal = abs(now[0] - goal[0]) + abs(now[1] - goal[1])
        flag_walk = True
        for circle in circles:
            now_circled = [2*circle[0] - now[0], 2*circle[1] - now[1]]
            if now_circled[0] < 0 or now_circled[0] > n-1 or now_circled[1] < 0 or now_circled[1] > n-1:
                continue
            dist_circled = abs(now_circled[0] - goal[0]) + abs(now_circled[1] - goal[1]) + 1
            if dist_circled < dist_goal:
                flag_walk = False
                move.append(f'J {circle[0]} {circle[1]}')
                circles.remove(circle)
                circles.append(now)
                queue.append((now_circled, circles, move))
                break

        if flag_walk:
            if random.random() < 0.5:
                if now[0] < goal[0]:
                    move.append('D')
                    queue.append(([now[0] + 1, now[1]], circles, move))
                elif now[0] > goal[0]:
                    move.append('U')
                    queue.append(([now[0] - 1, now[1]], circles, move))
                elif now[1] < goal[1]:
                    move.append('R')
                    queue.append(([now[0], now[1] + 1], circles, move))
                elif now[1] > goal[1]:
                    move.append('L')
                    queue.append(([now[0], now[1] - 1], circles, move))
            else:
                if now[1] < goal[1]:
                    move.append('R')
                    queue.append(([now[0], now[1] + 1], circles, move))
                elif now[1] > goal[1]:
                    move.append('L')
                    queue.append(([now[0], now[1] - 1], circles, move))
                elif now[0] < goal[0]:
                    move.append('D')
                    queue.append(([now[0] + 1, now[1]], circles, move))
                elif now[0] > goal[0]:
                    move.append('U')
                    queue.append(([now[0] - 1, now[1]], circles, move))


    return now, circles, move

def solve(n, m, k, t, s, goals):
    now = s
    circles_init = []
    for k in range(k):
        circles_init.append([random.randint(0, n-1), random.randint(0, n-1)])
    circles = circles_init.copy()
    move = []
    for goal in goals:
        now, circles, move = one_step(n, k, now, goal, circles, move)
    return circles_init, move

def main():
    n, m, k, t, s, goals = input_all()
    time_start = time.time()
    move_ans = None
    circles_ans = None
    while True:
        circles, move = solve(n, m, k, t, s, goals)
        if move_ans is None or len(move) < len(move_ans):
            move_ans = move
            circles_ans = circles
        if time.time() - time_start > 1.8:
            break
    output_all(circles_ans, move_ans)

if __name__ == '__main__':
    main()
