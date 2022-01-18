# 이진트리(BinaryTree)

# 순회 : 이진트리의 key값을 모두 출력하는 것
# 1. pre_order : Mid -> Left -> Right
# 2. in_order : Left -> Mid -> Right
# 3. post_order : Left -> Right -> Mid

# 이진트리 노드 정의
class BinaryNode:
    def __init__(self, key=None, parent=None, left=None, right=None):
        self.key = key  # value
        self.parent = parent  # 부모 노드 주소값
        self.left = left    # 왼쪽 자식 노드 주소값
        self.right = right   # 오른쪽 자식 노드 주소값

    def __str__(self):
        return str(self.key)

    # def __iter__(self):
    #     if self:
    #         yield self.key
    #         if self.left:
    #             self.left.__iter__()
    #         if self.right:
    #             self.right.__iter__()



    # 재귀 호출
    # 현재 노드 = self
    def preorder(self):
        if self:
            print(self.key)
            if self.left:
                self.left.preorder()
            if self.right:
                self.right.preorder()

    def inorder(self):
        if self:
            if self.left:
                self.left.inorder()
            print(self.key)
            if self.rigt:
                self.right.inorder()

    def postorder(self):
        if self:
            if self.left:
                self.left.postorder()
            if self.right:
                self.right.postorder()
            print(self.key)
