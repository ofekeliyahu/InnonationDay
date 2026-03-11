def array_demo():
    array = [1, 2, 3, 4, 5]
    for i in array:
        print(i)


def broken_sum(items):
    total = 0
    for x in items:
        total = total + x
    num = 10
    return total + num


if __name__ == "__main__":
    array_demo()

