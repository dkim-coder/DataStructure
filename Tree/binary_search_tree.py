# 이진탐색트리
# 각 노드의 왼쪽 subtree의 key 값은 노드의 key 값보다 작거나 같아야하고 오른쪽은 커야 한다.

from binary_tree import BinaryNode as bn
import random


class Bst:
    def __init__(self):
        self.root = None    # 루트노드 주소
        self.size = 0

    def __len__(self):
        return self.size

    # def __iter__(self):
    #     return self.root.__iter__()

    # key 값을 갖는 노드주소 반환
    # 값이 없으면 부모가 될 노드 주소 반환
    def find_loc(self, key):
        if self.size == 0:
            return None
        p = None    # 부모 노드
        v = self.root   # 자식 노드
        while v != None:
            if v.key == key:
                return v
            elif v.key < key:
                p = v
                v = v.right
            else:
                p = v
                v = v.left
            return p

    def search(self, key):
        v = self.find_loc(key)
        if v == None:
            return None
        else:
            return v

    def insert(self, key):
        p = self.find_loc(key)
        if p == None or p.key != key:
            v = bn(key)     # key 값을 갖는 노드 생성
            if p == None:
                self.root = v
            else:
                v.parent = p
                if p.key >= key:
                    p.left = v
                else:
                    p.right = v
            self.size += 1
            return v
        else:
            print("key is already in tree")
            return None

    def delete_by_merging(self, x):    # 노드 x를 삭제
        if x != None