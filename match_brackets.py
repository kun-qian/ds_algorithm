#!usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Kun'


# strings only contain '(', ')'
def simple_checker(strings):
    s = []

    for v in strings:
        if v == '(':
            s.append(v)
        else:
            if len(s) != 0:
                s.pop()
            else:
                return False

    return len(s) == 0


# strings contain ()[]{}
def checker(strings):
    s = []
    for v in strings:
        if v in '([{':
            s.append(v)
        else:
            if len(s) == 0:
                return False
            else:
                if not match(s.pop(), v):
                    return False
    return len(s) == 0


def match(open_tag, close_tag):
    opens = '{[('
    closes = '}])'
    return opens.index(open_tag) == closes.index(close_tag)

# print(simple_checker("(())()())"))
# print(simple_checker('((()))'))
print(checker('{[()]}'))
