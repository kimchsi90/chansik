class Node:
    def __init__(self, data):
        self.data = data # 값을 기리키는 변수(속성, attribute)
        self.next = None # 다음 노드를 가리키는 변수


head = Node(1)
head.next = Node(2)
head.next.next = Node(3)

node = head

# 연결 리스트의 값 출력하기
def my_print(node):
    while node: # node가 None이 아닐 때 까지
        print(node.data, end=" ")
        node = node.next

my_print(node)

# 연결 리스트의 값 추가하기
def add(node, data):
    while node:
        if node.next == None:
            node.next = Node(data)
            break
        node = node.next

add(node, 4)

# 연결 리스트의 처음에 새 노드를 추가하기
node = Node(0) # 0번째 노드를 생성
node.next = head # 0번째 노드의 다음 노드를 1번째 노드로 설정
head = node # linked list의 head를 0번째 노드로 설정


'''
연결 리스트의 구조와 특징
연결 리스트는 여러 곳의 자료를 연결한 것이다. 연결 리스트는 배열처럼 선형 자료 구조이지만, 연속한 메모리 위치에 값이 저장되는 것은 아니다.

단일 연결 리스트(Singly Linked List)는 아래 그림처럼 노드(Node)를 연결한 것으로, 노드는 값과 다음 노드의 주소를 저장한다. 그리고 C 언어의 배열 이름이 첫째 원소의 주소를 가리키는 것처럼, 연결 리스트에서는 head가 첫째 노드의 주소를 가리킨다.
'''
