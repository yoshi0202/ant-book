n = 4
a = [1, 2, 4, 7]
k = 15


def dfs(r, sum):
    # print("r", r)
    # print("sum", sum)
    if(r == n - 1):
        if(sum == k):
            return True
        else:
            return False
    if (dfs(r+1, sum)):
        return True
    if (dfs(r+1, sum + a[r])):
        return True

    return False


if __name__ == "__main__":
    r, sum = 0, 0
    print(dfs(r, sum))
