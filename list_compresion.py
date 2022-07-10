import numbers


def run():
    square = [i for i in range(1, 10000) if i % 36 == 0]
    print(square)


if __name__ == '__main__':
    run()
