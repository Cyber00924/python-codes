words = ["hello", "world", "Python", "programming", "is", "fun"]
n = 5
result = []

for word in words:
    if len(word) > n:
        result.append(word)

print(f"Words longer than {n} characters:", result)
