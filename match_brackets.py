#!usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'kun qian'


# if the string only contains '(', ')'
# tell if the text match ()
def match_bracket(text):
    stack = []
    for v in text:
        if v == '(':
            stack.append(v)
        else:
            if len(stack) == 0:
                return False
            else:
                stack.pop()
    return len(stack) == 0

print(match_bracket('((())()())'))


def match_all_brackets(text):
    s = []
    for v in text:
        if v in '([{':
            s.append(v)
        else:
            if len(s) == 0:
                return False
