"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)"""

'''
You are given a pointer to the root
of a binary search tree and a value to be inserted into the tree.
 Insert this value into its appropriate position in the binary
 search tree and return the root of the updated binary tree. You just have to complete the function.
 '''
def insert(r,val):
    if not r:
        return Node(val)

    else:
        if r.data<=val:
            r.right=insert(r.right,val)
        elif r.data>val:
            r.left=insert(r.left,val)
    return r
