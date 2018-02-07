#!usr/bin/env python3
# -*- coding: utf-8 -*-


def recMC(coinValueList, change):
    min_coins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c < change]:
            counts = 1 + recMC(coinValueList, change - i)
            if counts < min_coins:
                min_coins = counts
    return min_coins


def recDC(coinValueList, change, knownResults):
    min_coins = change
    if change in coinValueList:
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c < change]:
            counts = 1 + recDC(coinValueList, change - i, knownResults)
            if counts < min_coins:
                min_coins = counts
                knownResults[change] = min_coins
        return min_coins


# print(recMC([1, 5, 10, 25], 63))
print(recDC([1, 5, 10, 25], 63, [0] * 64))
