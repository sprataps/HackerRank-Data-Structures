""" Node is defined as
class node:
  def __init__(self, data):
      self.data = data
      self.left = None
      self.right = None
"""
def minValue(node):
    if not node:
        return 2**8
    else:
        return min(minValue(node.left),minValue(node.right))

def maxValue(node):
    if not node:
        return -(2**8)
    else:
        return max(maxValue(node.left),maxValue(node.right))

def check_binary_search_tree_(root):
    if not root:
        return True
    if root.left:
        if maxValue(root.left)>root.data:
            return False
        else:
            return check_binary_search_tree_(root.left)
    if root.right:
        if minValue(root.right)<root.data:
            return False
        else:
            return check_binary_search_tree_(root.right)
    return True


        
