class node():
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None    
    
    def insert(self, data):
        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

    def printTree(self):
        if self.left:
            self.left.printTree()
        print( self.data),
        if self.right:
            self.right.printTree()

alphabet = "abcdefghijklmnopqrstuvwxyz"
lst = "a?b?c:d:e"

for i,val in lst:
    if val in enumerate(alphabet):
        print(val)
