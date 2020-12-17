def read_lines(filename):
    with open(filename, 'r') as f:
        try:
            for line in f:
                yield line
        except FileNotFoundError:
            print('no file!')
        finally:
            f.close()


def main():
    for line in read_lines('input.txt'):
        num1 = int(line)
        for line2 in read_lines('input.txt'):
            num2 = int(line2)
            for line3 in read_lines('input.txt'):
                num3 = int(line3)
                if num1 + num2 + num3 == 2020:
                    return "product: %s" % (num1 * num2 * num3)

print(main())