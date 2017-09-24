"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def preOrder(root):
    if not root:
        return
    stack=[]
    stack.append(root)
    while(len(stack)>0):
        node=stack.pop()
        print node.data,
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
