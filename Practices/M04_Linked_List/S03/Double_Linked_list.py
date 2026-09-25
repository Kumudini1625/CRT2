'''
1.data
2.prev
3.next
Algorithm:
1.Create node
2.insert node
3.connection
4.traverse
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
node1=Node(10)
node2=Node(20)
node3=Node(30)
node4=Node(40)

node1.next=node2
node2.prev=node1

node2.next=node3
node3.prev=node2

node3.next=node4
node4.prev=node3

def traverse():
    curr=node1
    while curr:
        print(curr.data , end="<->")
        curr=curr.next
    print("None")
traverse()


#reverse traverse
def reverse_traverse():
    curr=node4
    while curr:
        print(curr.data , end="<->")
        curr=curr.prev
    print("None")
reverse_traverse()

#insertion at beginning
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
def insert_begin(head, data):
    new_node=Node(data)
    new_node.next=head
    if head:
        head.prev=new_node
    return new_node
def traverse(head):
    curr=head
    while curr:
        print(curr.data , end="<->")
        curr=curr.next
    print("None")
head=None
head=insert_begin(head, 50)
head=insert_begin(head, 60)
head=insert_begin(head, 70)
print("Insertion at beginning:")
traverse(head)  
print()