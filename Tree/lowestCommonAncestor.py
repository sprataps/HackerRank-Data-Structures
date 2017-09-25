"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def lca(root , v1 , v2):

    node=root
    p=[]
    p.append(root)
    while(node):
        if v1<node.data and v2>node.data:
            return p.pop()
        elif v1>node.data and v2<node.data:
            return p.pop()
        else:
            if v1==node.data or v2==node.data:
                return node
            if v1<node.data and v2<node.data:
                node=node.left
            else:
                node=node.right
        p.append(node)



        
