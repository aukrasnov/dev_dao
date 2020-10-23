# Восстановите строку по её коду и беспрефиксному коду символов.
# В первой строке входного файла заданы два целых числа  k k и  l l через пробел — количество различных букв,
# встречающихся в строке, и размер получившейся закодированной строки, соответственно.
# В следующих  k k строках записаны коды букв в формате "letter: code".
# Ни один код не является префиксом другого. Буквы могут быть перечислены в любом порядке.
# В качестве букв могут встречаться лишь строчные буквы латинского алфавита;
# каждая из этих букв встречается в строке хотя бы один раз. Наконец, в последней строке записана закодированная строка.
# Исходная строка и коды всех букв непусты. Заданный код таков,
# что закодированная строка имеет минимальный возможный размер.
# В первой строке выходного файла выведите строку  s s.
# Она должна состоять из строчных букв латинского алфавита.
# Гарантируется, что длина правильного ответа не превосходит  1 0 4 10  4   символов.


def read_input():
    count_letters, code_length = tuple(input().split(' '))

    letters_dict = {}
    for i in range(int(count_letters)):
        input_list = input().split(': ')
        letters_dict[input_list[0]] = input_list[1]

    code = str(input())

    return letters_dict, code


def haffman_decoder(letters_dict, code):
    reverse_dict = {v: k for k, v in letters_dict.items()}

    answer = ''
    value = ''
    for i in code:
        value += i
        if value in reverse_dict:
            answer += reverse_dict[value]
            value = ''

    return answer


def main():
    letters_dict, code = read_input()
    # letters_dict, code = ({'a': '0', 'b': '10', 'c': '110', 'd': '111'}, '01001100100111')
    # letters_dict, code = ({'a': '0'}, '0')

    return haffman_decoder(letters_dict, code)


if __name__ == "__main__":
    # main()
    print(main())
