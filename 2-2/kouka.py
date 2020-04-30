if __name__ == "__main__":
    dict = {
        500: [1, 1],
        100: [],
        50: [1, 1, 1],
        10: [1],
        5: [1, 1],
        1: [1, 1, 1]
    }

    A, result, cnt = 620, 0, 0
    for i in dict:
        for n in dict[i]:
            if A >= result + i:
                result += i
                cnt += 1
    print(cnt)
