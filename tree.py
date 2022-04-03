import sys
import os
from pathlib import Path
from my_tree import n_ary_tree
import traversals.PreOrderTraversal as PreOrder
from validator import validate
from validator.exception import TreeException


def TreeGenerator(node, level):
    '''
    return an root N-ary Node which consist of all the childrens associated to it
    recursively.
    '''
    children = []
    try:
        children = [TreeGenerator(str(Path(node)/c), level+1)
                  for c in os.listdir(node) if c != None]
    except:
        pass
    return n_ary_tree.Node(node, children, level)


if __name__ == '__main__':
    input = sys.argv[1]

    try:
        validate.CheckInput(input)
    except TreeException as e:
        print(e)
        exit(1)

    root = TreeGenerator(str(input), 0)
    raw_response = []

    PreOrder.pre_order_traversal(root, raw_response, 0)
    PreOrder.format(raw_response)
