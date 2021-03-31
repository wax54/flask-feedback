start = 'a'
lookup = []


def next_try(input):
    last_char = input[-1]
    if(last_char == 'z'):
        input += 'a'
        return input
    input = input[:-1]
    new_char = chr(ord(last_char)+1)
    input += new_char
    return input


def test_it(input):
    for i in range(1000000):
        the_hash = hash(input)
        if the_hash in lookup:
            print('Match Found!', the_hash, input)
        else:
            lookup.append(the_hash)
        input = next_try(input)
