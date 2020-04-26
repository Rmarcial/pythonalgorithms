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
    if len(sentence) == 0 or len(sentence) == 1:
        return True
    else:
        return first_char(sentence) == last_char(sentence) \
               and is_palindrome_recur(middle(sentence))


# Utils
def first_char(sentence):
    return sentence[0]


def last_char(sentence):
    return sentence[len(sentence)-1]


def middle(sentence):
    return sentence[1:-1]


# Tests
stc = ""
for n in range(10001):
    stc += "a"

print(is_palindrome_iter(stc))
print(is_palindrome_recur(stc))





