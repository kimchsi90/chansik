# 파이썬으로 트리 구조를 구현할 때는 Node class 정의
class Node:
    def __init__(self, data, left_node, right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회(Preorder Traversal)
def pre_order(node):
    # 자기 자신의 데이터를 먼저 처리한 뒤에
    print(node.data, end=' ')
    # 이어서 왼쪽 노드와
    if node.left_node != None:
        pre_order(tree[node.left_node])
    # 오른쪽 노드를 방문
    if node.right_node != None:
        pre_order(tree[node.right_node])

# 중위 순회(Inorder Traversal)
def in_order(node):
    # 왼쪽을 먼저 방문한 뒤에
    if node.left_node != Node:
        in_order(tree[node.left_node])
    # 자기 자신의 데이터를 처리한 뒤에
    print(node.data, end=' ')
    # 오른쪽을 방문
    if node.right_node != None:
        in_order(tree[node.right_node])

# 후위 순회(Postorder Traversal)
def post_order(node):
    # 왼쪽을 먼저 방문
    if node.left_node != None:
        post_order(tree[node.left_node])
    # 그 다음 오른쪽을 방문
    if node.right_node != None:
        post_order(tree[node.right_node])
    # 마지막으로 자기 자신을 처리
    print(node.data, end=' ')

# 노드의 개수
n = int(input())
tree = {} # 트리는 dict를 이용하여 구현

for i in range(n):
    data, left_node, right_node = input().split()
    if left_node == "None":
        left_node = None
    if right_node == "None":
        right_node = None
    # data는 tree에 담고 각 노드는 자기 자신의 data와 left_node, right_node를 담음
    tree[data] = Node(data, left_node, right_node)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])

''' 입력 예시
7
A B C
B D E
C F G
D None None
E None None
F None None
G None None
'''