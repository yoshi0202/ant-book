import sys

args = sys.argv


def fib(n, dict):
    if(n in dict):
        return dict[n]
    if (n == 0):
        return 0
    if (n < 3):
        return 1
    dict[n] = fib(n - 2, dict) + fib(n - 1, dict)
    return dict[n]


if __name__ == "__main__":
    dict = {}
    if(len(args) < 2):
        print("Valid")
    else:
        print(fib(int(args[1]), dict))
