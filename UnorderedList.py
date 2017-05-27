#!usr/bin/env python3
# -*- coding: utf-8 -*-


class Node:
    def __init__(self, init_value):
        self.value = init_value
        self.next = None

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, next):
        self.next = next


class UnorderedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def add(self, item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0

        while current is not None:
            count += 1
            current = current.get_next()

        return count

    def search(self, item):
        current = self.head
        found = False

        while current is not None and not found:
            if item == current.get_value():
                found = True
            else:
                current = current.get_next()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while current is not None and not found:
            if current.get_value() == item:
                found = True
            else:
                previous = current
                current = current.get_next()

        if found:
            if previous == None:
                self.head = None
            else:
                previous.set_next(current.get_next())


    def __str__(self):
        l = []
        current = self.head
        while current is not None:
            l.append(current.get_value())
            current = current.get_next()

        return str(l)


m = UnorderedList()
m.add(1)
m.add(2)
m.add('3')
m.add('ha')
m.add(True)
# print(m)
m.remove(4)
print(m)
