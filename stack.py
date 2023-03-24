#! /usr/bin/python3
"""
    Stack Data Structure
"""

class Stack():
    def __init__(self):
        self.items = []

    # push method that will append on the list 
    def push(self, item):
        self.items.append(item)


print(Stack.push('Joseph'))