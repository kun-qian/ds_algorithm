#!usr/bin/env python3
# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, value):
        self.data = value
        self.next = None

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next

    def set_next(self, node):
        self.next = node


class OrderedList(object):

    def __init__(self):
        self.head = None

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def is_empty(self):
        return self.head is None

    def add(self, value):
        current = self.head
        previous = self.head
        while current is not None:
            if current.get_data() < value:
                previous = current
                current = current.get_next()
            else:
                break

        node = Node(value)
        if previous is None:
            node.set_next(self.head)
            self.head = node
        else:
            node.set_next(current)
            previous.set_next(node)

    def search(self, value):
        current = self.head
        while current is not None:
            if current.get_data() == value:
                return True
            else:
                if current.get_data() < value:
                    current = current.get_next()
                else:
                    return False
        return False

    def remove(self, value):
        previous = self.head
        current = self.head
        while current is not None:
            if current.get_data() == value:
                previous.set_next(current.get_next())
                break
            else:
                previous = current
                current = current.get_next()

    def __str__(self):
        l = []
        current = self.head
        while current is not None:
            l.append(current.get_data())
            current = current.get_next()
        return str(l)


l = OrderedList()
l.add(1)
l.add(43)
l.add(3)
l.remove(3)
print(l)
