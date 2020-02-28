class BinarySearchTree:
    #need three values for it to be a binary search tree
    #infinate loop vs recurssion- to be recurssion needs to have a base case and be moving towards that base case

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    #start here because we need to have something in the tree to do anything with it
    def insert(self, value):
        #if value is < node.value look left
        if value < self.value:
            # if something is there already
            if self.left:
                # recurse to the left
                    self.left.insert(value)
            # if not
            else:
                self.left = BinarySearchTree(value)
                #insert left
        #if value is >= node.value look right
        if value >= self.value:
            # if something is there already
            if self.right:
                # recurse to the right
                self.right.insert(value)
             # if not
            else:
                #insert right
                self.right = BinarySearchTree(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            if self.left:
                return self.left.contains(target)
            else:
                return False
        if target >= self.value:
            if self.right:
                return self.right.contains(target)
            else:
                return False