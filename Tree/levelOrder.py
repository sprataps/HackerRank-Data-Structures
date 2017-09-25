"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def levelOrder(root):
    stack=[]
    stack.append(root)
    for i in stack:
        if i.left:
            stack.append(i.left)
        if i.right:
            stack.append(i.right)
        if not i:
            break
    for i in stack:
        print i.data,
