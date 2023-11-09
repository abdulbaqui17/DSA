class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=next

class sll:
    def __init__(self):
        self.head=None

    def insert_first(self,data):
        n=node(data)
        n.next=self.head
        self.head=n
        
    def insert_last(self,data):
        n=node(data)
        current=self.head
        while current.next is not None:
            current=current.next
        current.next=n
    
    def insert_value(self,target,data):
        if self.head is None:
            print("list is empty")
        current=self.head
        while current is not None:
            if current.data==target:
                current.next=node(data,current.next)
                return
            current=current.next
            
    def delete_first(self):
        if self.head is None:
            print("list is empty")
        else:
            self.head=self.head.next
    
    def delete_last(self):
        if self.head is None:
            print("list is empty")
        else:
            current=self.head
            while current.next is None:
                current=current.next
            current.next.next=None
        
    def delete_value(self,data):
        if self.head.data==data:
            self.head=self.head.next
        else:
            current=self.head
            while current is not None:
                if current.next.data==data:
                    current.next=current.next.next
                    return
                current=current.next
                
    def display(self):
        if self.head is None:
            print("list is empty")
        n=self.head
        while n is not None:
            print(n.data,end=" ")
            n=n.next
    
    def __iter__(self):
        return slliterator(self.head)
    
class slliterator:
    def __init__(self,start):
        self.start=start
    def __iter__(self):
        return self
    def __next__(self):
        if self.start is None:
            raise StopIteration
        data=self.start.data
        self.start=self.start.next
        return data

l=sll()
l.insert_first(50)
l.insert_last(60)
l.insert_value(50,55)
l.insert_value(60,65)
l.insert_value(55,56)
#l.delete_first()
#l.delete_value(65)
#l.display()
for i in l:
    print(i,end=" ")
        