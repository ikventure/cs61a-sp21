# Tree ADT

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    if change_abstraction.changed:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return {'label': label, 'branches': list(branches)}
    else:
        for branch in branches:
            assert is_tree(branch), 'branches must be trees'
        return [label] + list(branches)


def label(tree):
    """Return the label value of a tree."""
    if change_abstraction.changed:
        return tree['label']
    else:
        return tree[0]


def branches(tree):
    """Return the list of branches of the given tree."""
    if change_abstraction.changed:
        return tree['branches']
    else:
        return tree[1:]


def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if change_abstraction.changed:
        if type(tree) != dict or len(tree) != 2:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True
    else:
        if type(tree) != list or len(tree) < 1:
            return False
        for branch in branches(tree):
            if not is_tree(branch):
                return False
        return True


def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)


def change_abstraction(change):
    change_abstraction.changed = change


change_abstraction.changed = False


def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)


def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

def same_shape(t1, t2):
    """Return True if t1 is indentical in shape to t2.

    >>> test_tree1 = tree(1, [tree(2), tree(3)])
    >>> test_tree2 = tree(4, [tree(5), tree(6)])
    >>> test_tree3 = tree(1,
    ...                   [tree(2,
    ...                         [tree(3)])])
    >>> test_tree4 = tree(4,
    ...                   [tree(5,
    ...                         [tree(6)])])
    >>> same_shape(test_tree1, test_tree2)
    True
    >>> same_shape(test_tree3, test_tree4)
    True
    >>> same_shape(test_tree2, test_tree4)
    False
    """
    "*** YOUR CODE HERE ***"
    