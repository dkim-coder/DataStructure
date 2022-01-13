# heap property 만족하는 이진트리
# level들이 가득 채워져있는 이진트리 모양 (마지막 level의 노드들은 왼쪽부터만 채워지면 된다.)
# heap 성질 : 모든 부모노드의 key 값은 자식노드의 key 값보다 작지 않다.

# H[k]의 왼쪽 자식 노드 index : H[2 * k + 1]
# H[k]의 오른쪽 자식 노드 index : H[2 * k + 2]
# H[k]의 부모 노드 index : H[(k -1) // 2]

import random

H = [random.randint(1, 100) for i in range(20)]   # heap 성질x 이진트리 가정

# heap 성질 이진 트리 만드는 함수
def make_heap(in_tree: list):
    n = len(in_tree)
    # 끝 노드부터 올라오면서 heap성질 만족 여부 수정
    for idx in range(n-1, -1, -1):
        heapify_down(in_tree, idx, n)

# k노드 부터 자식 노드들 heap 만족하도록 수정 함수
def heapify_down(A: list, k, n):
    while (k * 2 + 2) < n:  # 현재 노드가 leaf node가 아닌지 확인
        l, r = 2 * k + 1, 2 * k + 2
        m = A.index(max(A[k],A[l],A[r]))    # 최댓값 노드 index 구하기
        if k != m:
            A[k], A[m] = A[m], A[k]
            k = m
        else:
            break

make_heap(H)
print(H)
