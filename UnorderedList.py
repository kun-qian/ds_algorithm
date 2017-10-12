#!usr/bin/env python3
# -*- coding: utf-8 -*-


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def setData(self, data):
        self.data = data

    def getNext(self):
        return self.next

    def setNext(self, node):
        self.next = node


class UnorderedList(object):

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        new = Node(item)
        new.setNext(self.head)
        self.head = new

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            current = current.getNext()
            count += 1
        return count

    def search(self, value):
        current = self.head
        found = False
        while current is not None and not found:
            if current.getData() == value:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, value):
        previous = self.head
        current = self.head
        while current is not None:
            if current.getData() == value:
                previous.setNext(current.getNext())
                # current.setNext(None)
                break
            else:
                previous = current
                current = current.getNext()

    def __str__(self):
        l = []
        current = self.head
        while current is not None:
            l.append(current.getData())
            current = current.getNext()
        return str(l)

l = UnorderedList()
l.add(1)
l.add('a')
l.add(2)
print(l)
print(l.size())
print(l.search(1))
l.remove('a')
print(l)
l.add('haha')
print(l.size())
