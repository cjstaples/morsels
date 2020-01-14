#   This method can be used to check if two strings are anagrams.
#   An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
#   typically using all the original letters exactly once.

from collections import Counter


def is_anagram(first, second):
    return Counter(first) == Counter(second)


is_anagram("abcd3", "3acdb")  # True
