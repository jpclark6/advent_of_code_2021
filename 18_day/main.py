import re
from math import floor, ceil

with open('puzzle.txt', 'r') as f:
    numbers = f.read().split('\n')


def has_explosion(number):
    stack = []
    for i, n in enumerate(number):
        if n == '[':
            stack.append('[')
        elif n == ']':
            stack.pop()
        if len(stack) == 5:
            return True
    return False


def find_explosion_start(number):
    stack = []
    for i, n in enumerate(number):
        if n == '[':
            stack.append('[')
        elif n == ']':
            stack.pop()
        if len(stack) == 5:
            return i


def find_explosion_end(number, start_index):
    for i, n in enumerate(number[start_index:]):
        if n == ']':
            return start_index + i + 1


def has_split(number):
    match = re.search("[0-9][0-9]", number)
    if match:
        return True
    return False


def add_explosion(new_number, index, right_number, left_number):
    number = new_number[index-1:]
    match = re.search("[0-9]+", number)
    if match:
        value = str(int(match.group(0)) + right_number)
        start_index = match.start()
        end_index = match.end()
        r_number = f'{number[:start_index]}{value}{number[end_index:]}'
    else:
        r_number = new_number[index-1:]

    number = new_number[:index-2]
    number = number[::-1]
    match = re.search("[0-9]+", number)
    if match:
        value = str(int(match.group(0)[::-1]) + left_number)
        start_index = match.start()
        end_index = match.end()
        l_number = f'{number[:start_index]}{value[::-1]}{number[end_index:]}'[::-1]
    else:
        l_number = new_number[:index-2]
    return l_number + '0' + r_number


def explode(number):
    start_index = find_explosion_start(number)
    end_index = find_explosion_end(number, start_index)
    left_number, right_number = [int(n) for n in number[start_index+1:end_index-1].split(',')]

    new_number = number[:start_index] + '0' + number[end_index:]
    new_number = add_explosion(new_number, start_index + 2, right_number, left_number)

    return new_number


def split(number):
    match = re.search("[0-9][0-9]+", number)
    start_index = match.start()
    end_index = match.end()
    number_to_split = int(number[start_index:end_index])
    first_split = floor(number_to_split / 2)
    second_split = ceil(number_to_split / 2)
    new_number = f'[{first_split},{second_split}]'
    split_number = f'{number[:start_index]}{new_number}{number[end_index:]}'
    return split_number


def reduce_number(number):
    while(has_explosion(number) or has_split(number)):
        if has_explosion(number):
            number = explode(number)
            continue
        if has_split(number):
            number = split(number)
    return number


def add_numbers(x, y):
    return f'[{x},{y}]'


def reduce_magnitude(number):
    l_number = int(number[1:].split(',')[0])
    r_number = int(number[:-1].split(',')[1])
    return 3 * l_number + 2 * r_number


def find_magnitude(number):
    match = re.search('\[[0-9]+,[0-9]+\]', number)
    mag = reduce_magnitude(match.group(0))
    return number[:match.start()] + str(mag) + number[match.end():]


current_number = numbers.pop(0)

while numbers:
    next_number = numbers.pop(0)
    current_number = add_numbers(current_number, next_number)
    current_number = reduce_number(current_number)

while True:
    try:
        current_number = find_magnitude(current_number)
        mag = int(current_number)
        break
    except ValueError:
        continue

print("Part 1:", mag)


#  part 2

with open('puzzle.txt', 'r') as f:
    lines = f.read().split('\n')

max_mag = 0
for i, n1 in enumerate(lines):
    for j, n2 in enumerate(lines):
        if i == j:
            continue
        current_number = add_numbers(n1, n2)
        current_number = reduce_number(current_number)
        while True:
            try:
                current_number = find_magnitude(current_number)
                mag = int(current_number)
                break
            except ValueError:
                continue
        if mag > max_mag:
            max_mag = mag

print("Part 2:", max_mag)