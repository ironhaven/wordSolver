from itertools import permutations


def load_words():
    print('Parcing wordlist')
    with open('combined.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


def valdate_words(words):
    for i in filter(lambda x: x in word_list, words):
        yield i


def get_permutations_recurse1(chars):
    if len(chars) <= 2:
        return chars
    else:
        chars_split_1 = chars[:len(chars)//2]
        chars_split_2 = chars[len(chars)//2:]
        return get_permutations_recurse1(chars_split_1),
        get_permutations_recurse1(chars_split_2), chars


def get_permutations_recurse2(chars, len):
    # Recursive function that returns all string combnations in a tuple
    #
    if len == 3:
        # Base case
        string_combos = tuple([''.join(i) for i in permutations(chars, 3)])
        return tuple([''.join(i) for i in permutations(chars, 3)])
    else:
        # Next loop the permutations will be one shorter
        # This concatanates the tuples into a bigger tuple
        string_combos = tuple([''.join(i) for i in permutations(chars, len)])
        return string_combos + get_permutations_recurse2(chars, len - 1)


if __name__ == '__main__':
    word_list = load_words()
    print('Search wordlist for word')
    input_chars = input('Word: ')
    perms = get_permutations_recurse2(input_chars, len(input_chars))
    for i in filter(lambda x: x in word_list, perms):
        print(i)
