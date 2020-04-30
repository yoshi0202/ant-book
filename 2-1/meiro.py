import queue

meiro = [
    ["#", "S", "#", "#", "#", "#", "G", "#"],
    [".", ".", ".", ".", "#", ".", ".", "#"],
    [".", "#", ".", "#", ".", "#", ".", "#"],
    [".", "#", ".", ".", ".", ".", ".", "."],
    ["#", "#", ".", "#", ".", "#", ".", "#"],
    [".", ".", ".", "#", ".", "#", "#", "#"],
    [".", "#", "#", "#", ".", "#", ".", "#"],
    [".", ".", ".", "#", ".", ".", ".", "."],
    [".", "#", "#", "#", ".", "#", "#", "#"],
    [".", ".", ".", "#", ".", ".", ".", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "#"],
]


if __name__ == "__main__":
    INF = 999999
    start, que = [], []
    q = queue.Queue()
    vec = [[1, -1], [1, -1]]
    # for i in meiro:
    #     print(i)
    for y, _ in enumerate(meiro):
        que.append([])
        for x, m in enumerate(meiro[y]):
            if m == "S":
                que[y].append(0)
                start.append(y)
                start.append(x)
            else:
                que[y].append(INF)
    print("----------------")
    for i in que:
        print(i)
    print("----------------")

    # start位置から移動できる場所を調査
    # print(start)
    # start = [5, 1]
    que[start[0]][start[1]] = 0
    q.put(start)
    result = 0
    while not q.empty():
        now = q.get()
        if meiro[now[0]][now[1]] == "G":
            result = que[now[0]][now[1]]
            break
        # now[0] = 0 y軸
        # now[1] = 1 x軸
        for i, y in enumerate(vec):
            for n in y:
                if i == 0 and -1 < now[0] + n and now[0] + n < len(meiro):
                    # y座標
                    if not meiro[now[0]+n][now[1]] == "#" and que[now[0]+n][now[1]] == INF:
                        q.put([now[0]+n, now[1]])
                        que[now[0]+n][now[1]] = int(que[now[0]][now[1]]) + 1
                elif i == 1 and -1 < now[1] + n and now[1] + n < len(meiro[now[0]]):
                    # x座標
                    if not meiro[now[0]][now[1]+n] == "#" and que[now[0]][now[1]+n] == INF:
                        q.put([now[0], now[1]+n])
                        que[now[0]][now[1]+n] = int(que[now[0]][now[1]]) + 1
    for i in que:
        print(i)
    print("------------------")
    print(result)
