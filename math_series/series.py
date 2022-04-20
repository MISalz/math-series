
def series(num):
    return '1'


def fibonacci(n):
    f = [0, 1]
    for i in range(2, n+1):
        f.append(f[i-1]+f[1-2])
        return f[n]


def lucas(n):
    return '1'


def sum_series(n):
    return '1'
