class LinkedList():
    def __init__(self):
        self.head = None
        
    def insert_beg(self,data):
        node = Node(data,self.head)
        self.head = node
    
    def print(self):
        if self.head is None:
            print('the list is empty')
            return
        itr = self.head
        llist = ''
        while itr:
            llist += str(itr.data) +'-->'
            itr = itr.next
        print(llist)
    def insert_end(self,data):
        if self.head is None:
            self.head = Node
            print('no elements in the linked list')
            
