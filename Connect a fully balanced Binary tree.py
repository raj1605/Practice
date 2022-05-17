class Tree:

    def __init__(self, val):
        if(val == None):
            self.val = None
        else:
            self.val = val
            self.left = Tree(None)
            self.right = Tree(None)
        self.next = None

    def printN(self):
        print(self.val, self.left.val, self.right.val)

    def connect(self):

        parent = self
        child = parent.left
        
        while(parent != None and parent.val != None):
            parent.left.next = parent.right
            if(parent.next == None):
                
                parent.printN()
                parent.next = child
                parent = child
                if(parent.val != None and parent.left != None):
                    child = parent.left
                else:
                    child = None
                continue
            else:
                #parent.printN()
                parent.right.next = parent.next.left
                parent = parent.next

t = Tree(1)
t.left = Tree(-1)
t.right = Tree(10)
6t.left.left = Tree(11)
t.left.right = Tree(12)
t.right.left = Tree(13)
t.right.right = Tree(14)
t.connect()
print(t.val,t.next.val,t.next.next.val,t.next.next.next.val,t.next.next.next.next.val,t.next.next.next.next.next.val,t.next.next.next.next.next.next.val)
