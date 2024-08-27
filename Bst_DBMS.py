class BstNode:
    def __init__(self,key,value=None,parent=None):
            self.key=key
            self.value=value
            self.left=None
            self.right=None
            self.parent=parent
def find(node,key):
    if node is None:
        return None
    if key<node.key:
        find(node.left,key)
    elif key>node.key:
        find(node.right,key)
    elif node.key==key:
        return node.key,node.value
    else:
        return None
def length(node):
    if node is None:
        return 0
    return 1+length(node.left)+length(node.right)
    
def insert(node, key, value):
    if node is None:
        node = BstNode(key, value)
    elif key < node.key:
        node.left = insert(node.left, key, value)
        node.left.parent = node
    elif key > node.key:
        node.right = insert(node.right, key, value)
        node.right.parent = node
    return node
def balanceBst(node,left=0,right=None,parent=None):
    data=listAll(node)
    if right is None:
        right=len(data)-1
    if left>right:
        return None
    mid=(left+right)//2
    key,value=data[mid]
    root=BstNode(key,value)
    root.parent=parent
    root.left=balanceBst(node,left,mid-1,root)
    root.right=balanceBst(node,mid+1,right,root)
    return root
def listAll(node):
    if node is None:
       return []
    return listAll(node.left)+[(node.key,node.value)]+listAll(node.right)
def update(node,key,value):
    f=find(node,key)
    if f is None:
        return None
    node.key,node.value=key,value
    return f
def DisplayKey(node,space='\t',level=0):
    if node is None:
        print(space*level+'Φ')
        return 
    if node.left is None and node.right is None:
        print(space*level+str(node.key))
        return 
    DisplayKey(node.right,space,level+1) 
    print(space*level+str(node.key))
    DisplayKey(node.left,space,level+1)
class Treemap:
    def __init__(self):
        self.root=None
    def __setitem__(self,key,value):
        f=find(self.root,key)
        if not f:
            self.root=insert(self.root,key,value)
            balanceBst(self.root)
        else:
            update(self.root,key,value)
    def __getitem__(self,key):
        print(find(self.root,key))
    def __iter__(self):
        return (elem for elem in listAll(self.root))
    def __len__(self):
        return length(self.root)
    def display(self):
        return DisplayKey(self.root)
# bst=Treemap()
# bst.display()
# bst['ayush']='sample1@gmail.com'
# bst['james']='sample2@mail.com'
# bst['marco']='sample3@mail.com'
# bst.display()
# bst['ayush']
# l=len(bst)
# print(l)
# l=list(bst)
# print(l)
        