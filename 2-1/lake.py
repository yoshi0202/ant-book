lake = [
    ["W", "", "", "", "", "", "W", "W"],
    ["", "W", "W", "W", "", "W", "W", ""],
    ["", "", "W", "", "", "", "W", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "", "", "", "", "", "", ""],
    ["", "W", "", "", "", "", "", ""],
    ["W", "W", "W", "", "", "", "", ""],
    ["W", "W", "W", "", "", "", "", ""],
]


def dfs(x, y):
    if(lake[x][y] == "."):
        print("return")
        return
    lake[x][y] = "."
    for i in range(y-1, y+2):
        for n in range(x-1, x+2):
            if(-1 < i and -1 < n):
                if(i < len(lake) and n < len(lake[i])):
                    if(lake[n][i] == "W"):
                        dfs(n, i)
    return


if __name__ == "__main__":
    cnt = 0
    for i in lake:
        print(i)
    print("----------------")
    for i, l1 in enumerate(lake):
        for n, l2 in enumerate(l1):
            if(l2 == "W"):
                dfs(i, n)
                cnt += 1
    for i in lake:
        print(i)

    print(cnt)
