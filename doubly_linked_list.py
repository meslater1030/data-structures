#!/usr/bin/env python
from __future__ import unicode_literals

import os

class Node(object):
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class DoublyLinkedList(object):
    def __init__(self, itr=None):
        self.head = None
        self.tail = None
        self.length = 0
        if itr is not None:
            for item in itr:
                self.insert(item)

    def insert(self, val):
        """insert(val) will insert the value 'val'
        at the head of the list"""
        new_node = Node(val)
        if self.length == 0:
            self.tail = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
        self.head = new_node
        self.length += 1

    def append(self, val):
        """append(val) will append the value 'val'
        at the tail of the list"""
        new_node = Node(val)
        if self.length == 0:
            self.head = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
        self.tail = new_node
        self.length += 1

    def pop(self):
        """pop() will pop the first value off the head of
        the list and return it."""

        to_delete = self.head.val
        self.head = self.head.next
        self.head.prev = None
        self.length -= 1
        return to_delete

    def shift(self):
        """shift() will remove the last value
        from the tail of the list and return it.
        """
        to_delete = self.tail.val
        self.tail = self.tail.prev
        self.tail.next = None
        self.length -= 1
        return to_delete

    def remove(self, val):
        """will remove the first instance of 'val' found
        in the list, starting from the head. if 'val'
        is not present it will raise an appropriate Python
        exception."""
        cur = self.head
        while cur is not None:
            if cur.val == val:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                self.length -= 1
                return
            cur = cur.next
        raise LookupError("The value is not in the list.")
