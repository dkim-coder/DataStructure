# 양방향 연결 리스트

class Node:
    def __init__(self, key = None):
        self.key = key
        self.next = self
        self.prev = self

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0