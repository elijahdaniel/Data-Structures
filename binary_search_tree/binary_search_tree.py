"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if greater than or equal
        if value >= self.value:
            # check if .right exists
            # if so, make that node call insert with the same value
            if self.right:
                # call bst node with .insert passing the value
                self.right.insert(value)
            # if not, create a node with that value, set node as right child
            else:
                # create a new node
                new_node = BSTNode(value)
                # assign new node to .right
                self.right = new_node

        # else, go left
        else:
            # check if .left exists
            if self.left:
                # if so, make that node call insert with the same value
                self.left.insert(value)

            # if not, create a node right here
            else:
                self.left = BSTNode(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        # if self.value doesn't equal target
        elif target > self.value:
            if self.right:
                # return recurrsion
                return self.right.contains(target)
            # if we don't have self.right
            else:
                return False

        else:
            if self.left is not None:  # we have a left child
                return self.left.contains(
                    target
                )  # hand the target off to the left child
            # if we don't have a left child
            else:
                return False

    # Return the maximum value found in the tree
    def get_max(self):
        current_node = self

        while current_node.right is not None:
            current_node = current_node.right

        return current_node.value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:  # is not None is the same thing
            self.right.for_each(fn)

        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
