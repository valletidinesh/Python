class Node:
    def __init__(self,data):
        self.data = data
        self.link = None
class SingleLinkedList:
    def __init__(self):
        self.start = None
    def display_list(self):
        p = self.start
        if p is None:
            print("List is empty!")
            return
        print("List:")
        while p is not None:
            print(p.data,"",end = "")
            p = p.link
    def insert_at_beginning(self,data):
        temp = Node(data)
        temp.link = self.start
        self.start = temp
    def insert_at_end(self,data):
        temp = Node(data)
        p = self.start
        if p is None:
            self.start = temp
            return
        while p.link is not None:
            p = p.link
        p.link = temp
    def create_list(self):
        n = int(input("Enter the no of nodes:"))
        for i in range(n):
            data = int(input("Enter the data:"))
            self.insert_at_end(data)

list = SingleLinkedList()

list.create_list()
print("1.Insert_at_beginning:")
n = int(input())
if n == 1:
    data = int(input("enter data:"))
    list.insert_at_beginning(data)
list.display_list()
