"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

def topView(root):
    if not root:
        return
    stack=[]
    stack.append(root)
    while(stack[len(stack)-1].left):
        stack.append(stack[len(stack)-1].left)
    while(len(stack)>1):
        print stack.pop().data,
    #stack.append(root)
    while(stack[len(stack)-1].right):
        stack.append(stack[len(stack)-1].right)
    while(len(stack)>0):
        print stack.pop(0).data,
    
