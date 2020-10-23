pattern = input()
text = input()

p_len = len(pattern)
needed, current = sum(ord(c) for c in pattern), sum(ord(c) for c in text[:p_len])

for i in range(len(text) - p_len + 1):
    if needed == current and pattern == text[i:i + p_len]:
        print(i, sep=' ')

    current += ord(text[(i + p_len) % len(text)]) - ord(text[i])
