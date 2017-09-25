"""class Node:
    def __init__(self, freq,data):
        self.freq= freq
        self.data=data
        self.left = None
        self.right = None
"""


'''
Huffman coding assigns variable length codewords to fixed length input
characters based on their frequencies. More frequent characters are assigned
shorter codewords and less frequent characters are assigned longer codewords.
 A Huffman tree is made for the input string and characters are decoded based
  on their position in the tree. We add a '0' to the codeword when we move left
  in the binary tree and a '1' when we move right in the binary tree. We assign
  codes to the leaf nodes which represent the input characters.

For example :

        {ϕ,5}
     0 /     \ 1
    {ϕ,2}   {A,3}
   0/   \1
{B,1}  {C,1}
Input characters are only present on the leaves. Internal nodes have a character value of ϕ. Codewords:

A - 1
B - 00
C - 01
'''
# Enter your code here. Read input from STDIN. Print output to STDOUT
def decodeHuff(root , s):
    st=""
    node=root
    i=0
    while i<len(s):

        if s[i]=="1":
            node=node.right
        else:
            node=node.left
        if node.data!='\0':
            st+=str(node.data)
            node=root
        i+=1
    print st
