import little_helper
from more_itertools import take

input = little_helper.get_input(16, 2021).strip()


def parse_bits(input):
    for c in input:
        d = int(c, 16)
        b = f"{d:04b}"
        yield from (int(c) for c in b)


def bin2dec(bits):
    if len(bits) == 0:
        raise RuntimeError
    sum = 0
    for i, bit in enumerate(reversed(bits)):
        if bit:
            sum += 2**i
    return sum


def parse_packets(bits):
    while True:
        try:
            version = bin2dec(take(3, bits))
            type_id = bin2dec(take(3, bits))

            if type_id == 4:
                literal_value_bits = []

                while True:
                    group_prefix = bin2dec(take(1, bits))

                    literal_value_bits += take(4, bits)

                    if group_prefix == 0:
                        break

                literal_value = bin2dec(literal_value_bits)

                yield {"version": version,
                       "type_id": type_id,
                       "literal_value": literal_value}

            else:
                length_type_id = bin2dec(take(1, bits))

                if length_type_id == 1:
                    num_sub_packets = bin2dec(take(11, bits))

                    sub_packets = take(num_sub_packets, parse_packets(bits))
                else:
                    sub_packets_length = bin2dec(take(15, bits))

                    sub_packets_bits = take(sub_packets_length, bits)

                    sub_packets = list(parse_packets(iter(sub_packets_bits)))

                yield {"version": version,
                       "type_id": type_id,
                       "sub_packets": sub_packets}

        except (StopIteration, RuntimeError):
            return


def get_version_numbers(packets):
    for packet in packets:
        yield packet["version"]
        if "sub_packets" in packet:
            yield from get_version_numbers(packet["sub_packets"])


if __name__ == '__main__':
    bits = parse_bits(input)

    packets = list(parse_packets(bits))

    print(sum(get_version_numbers(packets)))
