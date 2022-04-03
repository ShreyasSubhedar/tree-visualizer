class Node:
    '''
    Data structure for the N-ary tree, where each parent node represents a 
    directory and each child node represents files or directories. 
    This data structure is optimal for describing file systems where,
    each parent node represents a directory and its first hierarchical children can be file/s or directories.
    '''

    def __init__(self, val=None, children=[], level=1):
        self.val = val
        self.children = children
        self.level = level
