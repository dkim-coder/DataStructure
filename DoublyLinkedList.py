# 양방향 연결 리스트

# 양방향 노드 정의
class Node:
    def __init__(self, key = None):
        self.key = key  # value
        self.next = self    # 이전 노드 주소값
        self.prev = self    # 다음 노드 주소값

# 양방향 연결 리스트 헤드 정의(더미 노드)
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0


    # a ~ b노드 만큼을 잘라서 x노드 뒤에 붙인다.
    # a노드와 b노드 사이에 head가 없어야 한다.
    def splice(self, a, b, x):  # a, b, x 3개의 노드
        ap = a.prev, bn = b.next, xn = x.next
        ap.next = bn
        bn.prev = ap
        xn.next = a
        a.prev = x
        b.next = xn
        xn.prev = b


    def moveAfter(self, a, x):  # a노드 x노드 뒤로 이동
        self.splice(a, a, x)

    def moveBefore(self, a, x): # a노드 x노드 앞으로 이동
        self.splice(a, a, x.prev)

    def insertAfter(self, x, key):  # x노드 뒤에 key값을 가진 새 노드 삽입
        self.moveAfter(Node(key), x)
        self.size += 1

    def insertBefore(self, x, key):
        self.moveBefore(Node(key), x) # x노드 전에 key값을 가진 새 노드 삽입
        self.size += 1

    def pushFront(self, key):
        self.insertAfter(self.head, key)

    def pushBack(self, key):
        self.insertBefore(self.head, key)

    def search(self, key):
        v = self.head
        while v.next != self.head:
            if v.key == key:
                return v
            v = v.next
        return None

    def remove(self, x):    # x노드 제거
        if x == None or x == self.head:
            return
        x.prev.next = x.next
        x.next.prev = x.prev
        del x
