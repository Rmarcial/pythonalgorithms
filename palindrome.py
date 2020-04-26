"""
 Algorithm to check if a sentence is a palindrome
 - iterative
 - recursive
"""


# Iterative
def is_palindrome_iter(sentence):
    reversed_sentence = sentence[::-1]
    for i in range(len(sentence)):
        if sentence[i] != reversed_sentence[i]:
            return False

    return True


# Recursive
def is_palindrome_recur(sentence):
    if len(sentence) <= 1:
        return True
    else:
        return sentence[0] == sentence[-1] \
               and is_palindrome_recur(sentence[1:-1])


# Tests
stc = "aaab baaa"
# for n in range(1000):
#    stc += "a"

print(is_palindrome_iter(stc))
print(is_palindrome_recur(stc))





