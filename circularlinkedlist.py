class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class CircularLinkedList:
    def __init__(self):
        self.last = None
    def display_list(self):
        if self.last is None:
            print("List is empty")
            return
        p = self.last.link
        while True:
            print(p.data," ",end = "")
            p = p.link
            if p == self.last.link:
                break
    def insert_at_beginning(self,data):
        temp = Node(data)
        temp.link = self.last.link
        self.last.link = temp
    def insert_in_empty_list(self,data):
        temp = Node(data)
        self.last = temp
        self.last.link = self.last
    def insert_at_end(self,data):
        temp = Node(data)
        temp.link = self.last.link
        self.last.link = temp
        self.last = temp
    def create_list(self):
        n = int(input("Enter no of nodes:"))
        if n == 0:
            return
        data = int(input("Enter first element:"))
        self.insert_in_empty_list(data)
        for i in range(n-1):
            data = int(input("Enter next element:"))
            self.insert_at_end(data)
    def delete_first_node(self):
        if self.last is None:
            return
        if self.last.link == self.last:
            self.last = None
            return
        self.last.link = self.last.link.link
    def delete_last_node(self):
        if self.last is None:
            return
        if self.last.link == self.last:
            self.last = None
            return
        p = self.last.link
        while p.link != self.last:
            p = p.link 
        p.link = self.last.link
        self.last = p
    def delete_node(self,x):
        if self.last is None:
            return
        if self.last.link == self.last and self.last.data == x:
            self.last = None
            return
        if self.last.link.data == x:
            self.last.link = self.last.link.link
            return
        p = self.last.link
        while p.link != self.last.link:
            if p.link.data == x:
                break
            p = p.link
        if p.link == self.last.link:
            print(x," is not found")
        else:
            p.link = p.link.link
            if self.last.data == x:
                self.last = p

list = CircularLinkedList()

while True:
    print("\n1.create_list")
    print("2.insert_at_beginning")
    print("3.insert_at_end")
    print("4.insert_in_empty_list")
    print("5.display_list")
    print("6.delete_first_node")
    print("7.delete_last_node")
    print("8.delete_node")
    print("9.Quit")
    
    n = int(input("Enter your choice:"))
    if n == 1:
        list.create_list()
    elif n == 2:
        data = int(input("Enter data:"))
        list.insert_at_beginning(data)
    elif n == 3:
        data = int(input("Enter data:"))
        list.insert_at_end(data)
    elif n == 4:
        data = int(input("Enter data:"))
        list.insert_in_empty_list(data)
    elif n == 5:
        list.display_list()
    elif n == 6:
        list.delete_first_node()
    elif n == 7:
        list.delete_last_node()
    elif n == 8:
        data = int(input("Enter data of the node to be deleted:"))
        list.delete_node(data)
    elif n == 9:
        break
