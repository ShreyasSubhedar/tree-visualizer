import os


def pre_order_traversal(root, result, level):
    '''
    The module provides the for Pre order traversal of any N-aray tree
    data struture
    '''
    if root is None:
        return
    result.append((root.val, root.level))
    for child in root.children:
        pre_order_traversal(child, result, level+1)


def format(result):
    '''
    pretty print the PreOrder traversal result to simulate a tree diagram
    for the given directory
    '''
    for n in result:
        tree_spaces_identifier = ''
        child_relation_identifier = ''
        if (n[1] == 0):
            print("{}{}{}".format(tree_spaces_identifier,
                  child_relation_identifier, os.path.basename(os.path.normpath(n[0]))))

        else:
            tree_spaces_identifier += '|  ' * (n[1])
            child_relation_identifier = '└──'
            print("{}{}{}".format(tree_spaces_identifier,
                  child_relation_identifier, os.path.basename(n[0])))
