from collections import Counter

n = int(input())
word_input = []
for i in range(n):
    words = input()
    word_input.append(words)
count = list(Counter(word_input).values())
print(len(count))
print(*count)
