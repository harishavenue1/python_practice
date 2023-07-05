cube = lambda x: x ** 3


def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0:
        return []

    fb = [0, 1]

    if n == 1:
        return [0]
    elif n == 2:
        return fb
    else:
        for i in range(2, n):
            fb.append(fb[i - 1] + fb[i - 2])
        return fb


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
