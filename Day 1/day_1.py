from utility.read_file import ReadFile

def main():
    for line in ReadFile.read_lines('input.txt'):
        num1 = int(line)
        for line2 in ReadFile.read_lines('input.txt'):
            num2 = int(line2)
            for line3 in ReadFile.read_lines('input.txt'):
                num3 = int(line3)
                if num1 + num2 + num3 == 2020:
                    return "product: %s" % (num1 * num2 * num3)

print(main())