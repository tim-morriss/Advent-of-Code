def read_lines(filename):
    with open(filename, 'r') as f:
        try:
            for line in f:
                yield line
        except FileNotFoundError:
            print('no file!')
        finally:
            f.close()


def part_one():
    passwords = {}
    true_count = 0
    for line in read_lines('input.txt'):
        print('----')
        rule, password = line.split(':')
        password = password.split(' ')[1].split('\n')[0]
        print(password)
        min, max = rule.split(' ')[0].split("-")
        letter = rule.split(":")[0].split(' ')[1]
        print("letter: %s min: %s max: %s" % (letter, min, max))
        count = 0
        for char in password:
            count += 1

        if count < int(min) or count > int(max):
            passwords[password] = False
        else:
            passwords[password] = True
            true_count += 1
    return true_count


def part_two():
    valid_count = 0
    for line in read_lines('input.txt'):
        # print('----')
        rule, password = line.split(':')
        password = password.split(' ')[1].split('\n')[0]
        # print(password)
        min, max = rule.split(' ')[0].split("-")
        letter = rule.split(":")[0].split(' ')[1]
        # print("letter: %s min: %s max: %s" % (letter, min, max))
        count = 0
        true_count = 0
        for char in password:
            count += 1
            if count == int(min) or count == int(max):
                if letter == char:
                    true_count += 1
        if true_count == 1:
            valid_count += 1
            # print("True! Valid count: %s" % valid_count)
    return valid_count


# print(part_one())
print(part_two())
