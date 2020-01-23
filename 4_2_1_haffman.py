# По данной непустой строке  s s длины не более  1 0 4 10  4  , состоящей из строчных букв латинского алфавита,
# постройте оптимальный беспрефиксный код.
# В первой строке выведите количество различных букв  k k, встречающихся в строке,
# и размер получившейся закодированной строки. В следующих  k k строках запишите коды букв в формате "letter: code".
# В последней строке выведите закодированную строку.


def read_input():
    string = str(input())
    return string


def tree_decoder(letters_sorted: dict, answer_dict, current_path='',):

    for i in letters_sorted:
        if i not in [0, 1, '0', '1']:
            answer_dict[i] = current_path
        else:
            new_path = current_path + str(i)
            tree_decoder(letters_sorted[int(i)][0], answer_dict, new_path)
    return answer_dict


def haffman(input_string):
    letters_list = sorted(list(input_string))
    prev_letter = letters_list[0]
    unique_letter_position = 0
    letters_sorted = [(letters_list[0], 1)]

    for i in letters_list[1:]:
        if i == prev_letter:
            letters_sorted[unique_letter_position] = (i, letters_sorted[unique_letter_position][1] + 1)
        else:
            unique_letter_position += 1
            letters_sorted.append((i, 1))
        prev_letter = i

    if len(letters_sorted) == 1:
        return input_string.replace(letters_list[0][0], '0'), 1, {letters_list[0][0]: '0'}

    letters_sorted = [i for i in sorted(letters_sorted, key=lambda x: x[1])]

    while len(letters_sorted) > 1:
        haffman_dict = {0: letters_sorted.pop(0), 1: letters_sorted.pop(0)}
        haffman_dict = (haffman_dict, str(int(haffman_dict[0][1]) + int(haffman_dict[1][1])))
        letters_sorted.insert(0, haffman_dict)
        letters_sorted = [i for i in sorted(letters_sorted, key=lambda x: int(x[1]))]

    letters_dict = tree_decoder(letters_sorted[0][0], {}, '')

    haffman_code = ''
    for i in input_string:
        haffman_code += letters_dict[i]

    return haffman_code, unique_letter_position + 1, letters_dict


def main():
    # data = read_input()
    data = 'a'

    return haffman(data.strip())


if __name__ == "__main__":
    haffman_code, count_letters, letters_dict = main()
    print(count_letters, len(haffman_code), sep=' ')
    for i in letters_dict:
        print('{}: {}'.format(i, letters_dict[i]))
    print(haffman_code)



