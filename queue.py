#!usr/bin/env python3
# -*- coding: utf-8 -*-

from pythonds.basic.queue import Queue


def hot_potato(names, num):
    queue = Queue()

    for i in names:
        queue.enqueue(i)

    while queue.size() > 1:
        for i in range(num):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    return queue.dequeue()


print(hot_potato(['A', 'B', 'C', 'D', 'E', 'F'], 3))


def josephus(num_persons, num):
    queue = Queue()

    for i in range(num_persons):
        queue.enqueue(i + 1)
    while queue.size() > 2:
        for i in range(num - 1):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    return queue


q = josephus(41, 3)
res = []
while q.size() > 0:
    res.append(q.dequeue())
print(res)
