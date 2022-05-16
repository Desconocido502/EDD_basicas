class Node:
    def __init__(self,data=None,next_node=None):
        self.data = data
        self.next_node = next_node
    
    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next_node
    
    def set_next(self,new_node):
        self.next_node = new_node

class Queue:
    def __init__(self,head=None):
        self.head = head
    
    def enqueue(self,data):
        new_item = Node(data)
        current = self.head
        if current is None:
            self.head = new_item
        else:
            while current.get_next():
                current = current.get_next()
            current.set_next(new_item)
    
    def dequeue(self):
        current = self.head
        if current != None:
            self.head = current.get_next()
        else:
            print("Queue is empty.")
            
    def __len__(self):
        return len(self.temp)
    
    def is_empty(self):
        return self.head is None
    
    def print_queue(self):
        current = self.head
        self.temp = []
        while current:
            self.temp.append(current.get_data())
            current = current.get_next()
        print(self.temp)

q = Queue()
q.enqueue(15)
q.enqueue(20)
q.enqueue(25)
q.enqueue(30)
q.print_queue()