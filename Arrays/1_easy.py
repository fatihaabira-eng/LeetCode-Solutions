
def mergeAlternately(word1: str, word2: str) -> str:
    result = []
    i = 0
    while i < len(word1) or i < len(word2):
        if i < len(word1):
            result.append(word1[i])
        if i < len(word2):
            result.append(word2[i])
        i += 1
    return ''.join(result)

print(mergeAlternately("abc", "pqr"))  # Output: "apbqcr"
print(mergeAlternately("ab", "pqrs"))  # Output: "apbqrs"
print(mergeAlternately("abcd", "pq"))  # Output: "apbqcd"