from utility.read_file import ReadFile
import json

def part_one():
    valid_counter = 0
    entries = {}
    for line in ReadFile.read_lines('input.txt'):
        # detect blank line
        if line in ['\n', '\r\n']:
            # if entries['byr'] and entries['iyr'] and entries['eyr'] and entries['hgt'] and entries['hcl'] and entries['ecl'] and entries['pid']:
            if all(key in entries for key in ('byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')):
                print("Valid! entries: %s" % (json.dumps(entries)))
                valid_counter += 1
            entries = {}
        else:
            split_array = line.split(' ')
            for entry in split_array:
                entries[entry.split(':')[0]] = entry.split(':')[1].strip()
    return valid_counter

print(part_one())
