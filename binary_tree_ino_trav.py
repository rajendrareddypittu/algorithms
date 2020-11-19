class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
def bt_insert(root,val):
    if root==None:
        root=Node(val)
    elif val <root.val :
        if root.left!=None:
            bt_insert(root.left,val)
        else:
            root.left=Node(val)
    elif val>root.val:
        if root.right!=None:
            bt_insert(root.right,val)
        else:
            root.right=Node(val)
            
    else:
        print("Duplicate Entry",val)
def bt_print(root):
    if root==None:
        return
    print(root.val)
    bt_print(root.left)
    bt_print(root.right)
    
root=Node(27)
bt_insert(root,14)
bt_insert(root,35)
bt_insert(root,10)
bt_insert(root,19)
bt_insert(root,31)
bt_insert(root,42)
bt_print(root)


            o/p
    --------------
    27
14
10
19
35
31
42
>
