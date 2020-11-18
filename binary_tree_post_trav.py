class Node:
    def __init__(self,value):
        self.value=value
        self.left=None
        self.right=None
class Btree(Node):
    def __init__(self):
        self.root=None
    def insert_node(self,value):
        if self.root==None:
            self.root=Node(value)
        else:
            bt_insert(self.root,value)
    def print_tree(self):
        if self.root==None:
            print("Tree is empty")
        else:
            bt_print_tree(self.root)
            
def bt_insert(root,value):
    if value <root.value:
        if root.left!=None:
            bt_insert(root.left,value)
        else:
            root.left=Node(value)
    elif value > root.value:
        if root.right!=None:
            bt_insert(root.right,value)
        else:
            root.right=Node(value)
    else:
        print("duplicate entry")

def bt_print_tree(root):
    if root==None:
        return
       
    bt_print_tree(root.left)
    bt_print_tree(root.right)
    print(root.value) 
    
   
    
    
    
        
    

 
    

r=Btree()

r.print_tree()

r.insert_node(27)
r.insert_node(14)
r.insert_node(35)
r.insert_node(10)
r.insert_node(19)
r.insert_node(31)
r.insert_node(42)
r.print_tree()

pre: [27, 14, 10, 19, 35, 31, 42]
post: [10, 19, 14, 31, 42, 35, 27]
in: [10, 14, 19, 27, 31, 35, 42]



