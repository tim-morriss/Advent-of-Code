import json
import re

def part_one():
    val_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_counter = 0
    with open('input.txt', 'r') as f:
        lines = f.read().split('\n\n')
        for line in lines:
            entries = {}
            line = line.replace('\n', ' ').split()
            for entry in line:
                entries[entry.split(':')[0]] = entry.split(':')[1].strip()
            if all(key in entries for key in val_keys):
                print("Valid! entries: %s" % (json.dumps(entries, indent=4)))
                valid_counter += 1
            else:
                print("Invalid! entries: %s" % (json.dumps(entries, indent=4)))
        return valid_counter


def part_two():
    val_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    valid_counter = 0
    with open('input.txt', 'r') as f:
        lines = f.read().split('\n\n')
        for line in lines:
            entries = {}
            line = line.replace('\n', ' ').split()
            for entry in line:
                entries[entry.split(':')[0]] = entry.split(':')[1].strip()
            # print('-----')
            byr = re.match('(19[2-9][0-9])|(200[0-2])', str(entries.get('byr')))
            # print("byr: %s is %s" % (entries.get('byr'), bool(byr)))
            iyr = re.match('(20[1][0-9])|(2020)', str(entries.get('iyr')))
            # print("iyr: %s is %s" % (entries.get('iyr'), bool(iyr)))
            eyr = re.match('(202[0-9])|(2030)', str(entries.get('eyr')))
            # print("eyr: %s is %s" % (entries.get('eyr'), bool(eyr)))
            hgt = re.match('(1[5-8][0-9]cm|19[0-3]cm)|(59in|6[0-9]in|7[0-6]in)', str(entries.get('hgt')))
            hcl = re.match('#([0-9]|[a-f]){6}', str(entries.get('hcl')))
            ecl = entries.get('ecl') in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
            # print("ecl: %s is %s" % (entries.get('ecl'), bool(ecl)))
            pid = re.match('[0-9]{9}', str(entries.get('pid')))
            if byr and iyr and eyr and hgt and hcl and ecl and pid:
                print("Valid! entries: %s" % (json.dumps(entries, indent=4)))
                valid_counter += 1
            else:
                # print("Invalid! entries: %s" % (json.dumps(entries, indent=4)))
                continue
        return valid_counter


# print(part_one())
print(part_two())
