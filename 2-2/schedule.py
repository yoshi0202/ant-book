if __name__ == "__main__":
    n = 5
    s = [1, 3, 6, 5, 8]
    t = [8, 5, 7, 9, 10]
    dict = {}
    for i in range(n):
        dict[s[i]] = t[i]

    s, e = 0, 0
    res = []
    for start, end in sorted(dict.items(), key=lambda x: x[1]):
        if e < start:
            e = end
            res.append(start)
    print(res)
