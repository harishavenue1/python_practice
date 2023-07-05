cube = lambda x: x ** 3


def fibonacci(n):
    # return a list of fibonacci numbers
    # fb = [0, 1]
    # for i in range(2, n):
    #     fb.append(fb[i - 1] + fb[i - 2])
    # return fb[0:n]

    # or

    a, b = 0, 1
    for i in range(n):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
