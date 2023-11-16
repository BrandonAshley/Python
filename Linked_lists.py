class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        

class LinkedList:
    def __init__(self):
        self.head=None
        
    def append(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head =new_node
            return
        last_node=self.head
        while last_node.next:
            last_node=last_node.next
        
        last_node.next=new_node
        
    def headIndsert(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
        
    def search(self,target):
        here=self.head
        
        while here:
            if here.data==target:
                return True
            here=here.next
        return False
    
    def insert(self,after,data):
        new_node = Node(data)
        
        if after == 0:
            new_node.next = self.head
            self.head = new_node
            return

        current = self.head
        count = 0
        while current:
            if count == after - 1:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            count += 1   
            
    def delete(self, data):
        current = self.head

        # If the node to be deleted is the head node
        if current and current.data == data:
            self.head = current.next
            return

        prev = None
        while current and current.data != data:
            prev = current
            current = current.next

        if current is None:
            print(f"Node with data {data} not found.")
            return

        prev.next = current.next            
        
    def display(self):
        current=self.head
        while current:
            print(current.data,end=" -> ")
            current=current.next
        print("None")

linkedlst=LinkedList()

linkedlst.append(1)
linkedlst.append(2)
linkedlst.append(3)

linkedlst.display()

linkedlst.headIndsert(4)
linkedlst.display()

search_result=linkedlst.search(2)
print(search_result)
search_result=linkedlst.search(5)
print(search_result)
    
linkedlst.insert(2, 6)
linkedlst.display()

linkedlst.delete(1)
linkedlst.display()
