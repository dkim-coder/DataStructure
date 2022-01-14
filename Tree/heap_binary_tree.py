# heap property 만족하는 이진트리
# level들이 가득 채워져있는 이진트리 모양 (마지막 level의 노드들은 왼쪽부터만 채워지면 된다.)
# heap 성질 : 모든 부모노드의 key 값은 자식노드의 key 값보다 작지 않다.

# H[k]의 왼쪽 자식 노드 index : H[2 * k + 1]
# H[k]의 오른쪽 자식 노드 index : H[2 * k + 2]
# H[k]의 부모 노드 index : H[(k -1) // 2]

import random

class HeapBinaryTree:
    def __init__(self, tree: list = None):
        self.tree = tree
        self.size = len(tree)

    def __str__(self):
        return str(self.tree)

    # heap 성질 이진 트리 만드는 함수
    def make_heap(self):
        # 끝 노드부터 올라오면서 heap성질 만족 여부 수정
        for idx in range(self.size - 1, -1, -1):
            self.heapify_down(idx)

    # k노드 부터 자식 노드들 heap 만족하도록 수정 함수
    def heapify_down(self, k):
        while (k * 2 + 2) < self.size:  # 현재 노드가 leaf node가 아닌지 확인
            l, r = 2 * k + 1, 2 * k + 2
            m = self.tree.index(max(self.tree[k],self.tree[l],self.tree[r]))    # 최댓값 노드 index 구하기
            if k != m:
                self.tree[k], self.tree[m] = self.tree[m], self.tree[k]
                k = m
            else:
                break

    # 자식 노드와 부모노드 heap성질 비교해서 바꿔줌(key값 크기 비교)
    def heapify_up(self, k):
        while k > 0 and self.tree[(k - 1)//2] < self.tree[k]:
            self.tree[k], self.tree[(k - 1)//2] = self.tree[(k - 1)//2], self.tree[k]
            k = (k - 1)//2

    # 최댓값 리턴
    def find_max(self):
        return self.tree[0]

    # 최댓값 제거
    def delete_max(self):
        if self.size == 0:
            return None
        key = self.tree[0]
        self.tree[0], self.tree[-1] = self.tree[-1], self.tree[0]
        self.tree.pop()
        self.heapify_down(0)
        return key

H = [random.randint(1, 100) for i in range(20)]   # heap 성질x 이진트리 가정
h = HeapBinaryTree(H)
h.make_heap()
print(h)
print(h.find_max())
h.delete_max()
print(h)