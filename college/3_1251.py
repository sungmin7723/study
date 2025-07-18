word = input()
words = []

for i in range(1, len(word)):
    for j in range(i + 1, len(word)):
        part1 = ''.join(reversed(word[:i]))
        part2 = ''.join(reversed(word[i:j]))
        part3 = ''.join(reversed(word[j:]))
        words.append(part1 + part2 + part3)

print(sorted(words)[0])