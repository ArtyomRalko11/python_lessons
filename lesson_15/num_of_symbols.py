


def num_symbols(word):
    count = 0
    for i in word:
        count += 1

    return count


enter_string = str(input('Enter a string: '))

print(num_symbols(enter_string))
