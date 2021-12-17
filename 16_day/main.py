from math import prod

with open('puzzle.txt', 'r') as f:
    hex_input = f.read().strip()


def convert_to_binary(hex_input):
    hex_to_binary = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111',
    }
    binary = ''
    for c in list(hex_input):
        binary += hex_to_binary[c.upper()]
    return binary

BINARY = convert_to_binary(hex_input)
versions = 0


def process_packet(loc):
    global versions

    packet_version_binary = BINARY[loc:loc+3]
    packet_version = int(packet_version_binary, 2)
    versions += packet_version

    loc += 3

    packet_type_id_binary = BINARY[loc:loc+3]
    packet_type_id = int(packet_type_id_binary, 2)

    loc += 3

    if packet_type_id == 4:
        #  literal value
        number_binary = ''
        while BINARY[loc] == '1':
            number_binary += BINARY[loc+1:loc+5]
            loc += 5
        else:
            number_binary += BINARY[loc+1:loc+5]
            loc += 5
        number = int(number_binary, 2)
        return loc, number
    else:
        # operator
        subpacket_numbers = []
        if BINARY[loc] == '0':
            total_subpacket_bits_binary = BINARY[loc+1:loc+16]
            total_subpacket_bits = int(total_subpacket_bits_binary, 2)
            loc += 16
            end_loc = loc + total_subpacket_bits
            while loc < end_loc:
                loc, number = process_packet(loc)
                subpacket_numbers.append(number)
        else:
            total_subpackets_binary = BINARY[loc+1:loc+12]
            total_subpackets = int(total_subpackets_binary, 2)
            loc += 12
            while len(subpacket_numbers) < total_subpackets:
                loc, number = process_packet(loc)
                subpacket_numbers.append(number)

        if packet_type_id == 0:
            return loc, sum(subpacket_numbers)
        elif packet_type_id == 1:
            return loc, prod(subpacket_numbers)
        elif packet_type_id == 2:
            return loc, min(subpacket_numbers)
        elif packet_type_id == 3:
            return loc, max(subpacket_numbers)
        elif packet_type_id == 5:
            if subpacket_numbers[0] > subpacket_numbers[1]:
                return loc, 1
            return loc, 0
        elif packet_type_id == 6:
            if subpacket_numbers[0] < subpacket_numbers[1]:
                return loc, 1
            return loc, 0
        elif packet_type_id == 7:
            if subpacket_numbers[0] == subpacket_numbers[1]:
                return loc, 1
            return loc, 0


loc, part_2_answer = process_packet(0)

print("Part 1:", versions)
print("Part 2:", part_2_answer)
