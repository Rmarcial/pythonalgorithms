"""
 Using dictionary data type to store how many times each word appear
"""


def create_word_frequency(lyrics):
    """
    :param lyrics: string with song lyrics
    :return dictionary: words associated with their occurring frequency
    """
    word_dict = {}

    words = lyrics.split()
    for word in words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

    return word_dict


def most_common_words(lyrics):
    """
    :param lyrics: a string with song lyrics
    :return tuple of most common words and their frequency
    """
    most_common = []

    word_dict = create_word_frequency(lyrics)
    values = word_dict.values()
    best = max(values)

    for word in word_dict:
        if word_dict[word] >= best:
            most_common.append(word)

    return most_common, best  # accepted syntax for tuple


# Tests
song = "The world is a vampire, sent to drain " \
       "Secret destroyers, hold you up to the flames " \
       "And what do I get, for my pain? " \
       "Betrayed desires, and a piece of the game " \
       "Even though I know I suppose I'll show " \
       "All my cool and cold-like old job " \
       "Despite all my rage I am still just a rat in a cage " \
       "Despite all my rage I am still just a rat in a cage "

print(create_word_frequency(song))
print(most_common_words(song))
