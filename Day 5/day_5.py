from utility.read_file import ReadFile


def upper_lower(num_range, instruction):
    instruction = instruction.replace('L', 'F')
    instruction = instruction.replace('R', 'B')
    row_final = 0
    for char in instruction:
        diff = num_range[1] - num_range[0]
        if diff == 1:
            if char == 'F' and num_range[0] > row_final:
                row_final = num_range[0]
            elif char == 'B' and num_range[1] > row_final:
                row_final = num_range[1]
        elif char == 'F':
            num_range = (num_range[0], num_range[0] + round(diff / 2) - 1)
            # print("F! row number: %s " % str(num_range))
        elif char == 'B':
            num_range = (num_range[1] - round(diff / 2) + 1, num_range[1])
            # print("B! row number: %s " % str(num_range))
    return row_final


def day_5_part_one():
    total = 0
    for line in ReadFile.read_lines('day_5_input.txt'):
        row = line[:-4]
        row_final = upper_lower((0, 127), row)
        # print(row_final)
        column = line[-4:]
        column_final = upper_lower((0, 7), column)
        # print(column_final)
        product = (row_final * 8) + column_final
        if product > total:
            total = product
    return total


def day_5_part_two():
    product_list = []
    total = 0
    for line in ReadFile.read_lines('day_5_input.txt'):
        row = line[:-4]
        row_final = upper_lower((0, 127), row)
        # print(row_final)
        column = line[-4:]
        column_final = upper_lower((0, 7), column)
        # print(column_final)
        product = (row_final * 8) + column_final
        product_list.append(product)
    return sorted(set(range(11, 851)).difference(product_list))


print(day_5_part_one())
print(day_5_part_two())
