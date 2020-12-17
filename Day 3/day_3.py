def part_one(right=3, down=1):
    xpos = 0
    collision = 0
    with open('input.txt', 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines), down):
            # print(xpos)
            line = lines[i].split('\n')[0]
            if line[xpos] == '#':
                collision += 1
            xpos += right
            xpos = xpos % len(line)
    return collision

def part_two():
    slope1 = part_one(1, 1)
    slope2 = part_one(3, 1)
    slope3 = part_one(5, 1)
    slope4 = part_one(7, 1)
    slope5 = part_one(1, 2)
    print("slope1: %s, slope2: %s, slope3: %s, slope4: %s, slope5: %s" % (slope1, slope2, slope3, slope4, slope5))
    return slope1 * slope2 * slope3 * slope4 * slope5

print(part_one())
print(part_two())
