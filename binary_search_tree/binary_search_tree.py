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
        # Check if BST exists?

        # Check if inserting value less than root's value
        # If so, go left
        if value < self.value:
            if self.left is None:
                self.left = BSTNode(value)  # Create new node
            else:
                self.left.insert(value)     # <-- Recursion
        # Else, go right
        else:
            if self.right is None:
                self.right = BSTNode(value) # Create new node
            else:
                self.right.insert(value)    # <-- Recursion


    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Check if target == self.value
        # If so, return True
        if self.value == target:
            return True
        else:
            # Check if target < self.value. If so, move left
            if target < self.value:
                if self.left is None:  # End of the left line
                    return False
                else:
                    return self.left.contains(target)  # Recurse from here
            # Else, move right
            else:
                if self.right is None:  # End of the right line
                    return False
                else:
                    return self.right.contains(target)  # Recurse from here

    # Return the maximum value found in the tree
    def get_max(self):
        # Check only right branches until reaching a None for self.right
        # Return the value where this happens

        #print(self.value)

        if self.right is None:
            return self.value
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.right:
            self.right.for_each(fn)
        if self.left:
            self.left.for_each(fn)





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
