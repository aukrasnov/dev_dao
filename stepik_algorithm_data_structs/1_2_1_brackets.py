

def main(data):
    whitelist = set("[]{}()")
    queue = []
    opposite = {']': '[', '}': '{', ')': '('}
    i = 1

    for char in data:
        if char not in whitelist:
            pass
        elif char in ['[', '{', '(']:
            queue.append((char, i))
        elif not queue or queue[-1][0] != opposite[char]:
            return i
        else:
            queue.pop()

        i += 1

    return 'Success' if not queue else queue[-1][1]


def test():
    assert main("([](){([])})") == 'Success'
    assert main("()[]}") == 5
    assert main("{{[()]]") == 7
    assert main("{{{[][][]") == 3
    assert main("{*{{}") == 3
    assert main("[[*") == 2
    assert main("{*}") == 'Success'
    assert main("{{") == 2
    assert main("{}") == 'Success'
    assert main("") == 'Success'
    assert main("}") == 1
    assert main("*{}") == 'Success'
    assert main("{{{**[][][]") == 3


# test()
from_input = str(input())
print(main(from_input))
