#!usr/bin/env python3
# -*- coding: utf-8 -*-
from pythonds import Deque


def is_palindrome1(string):
    return str(string) == str(string)[::-1]


print(is_palindrome1(12321))


def is_palindrome2(string):
    char_deque = Deque()

    for i in str(string):
        char_deque.addRear(i)

    while char_deque.size() > 1:
        first = char_deque.removeFront()
        last = char_deque.removeRear()
        if first != last:
            return False
    return True


print(is_palindrome2('13231'))
print(is_palindrome2('abcb'))
