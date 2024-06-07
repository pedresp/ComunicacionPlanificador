class BST():
    def __init__(self, value : float, name : str):
        self.value = value
        self.name = name

        self.left = None
        self.right = None

    def add_node(bstree, bst):
        if bstree == None:
            return bst
        if bst.value > bstree.value:
            bstree.right = BST.add_node(bstree.right, bst)
        else:
            bstree.left = BST.add_node(bstree.left, bst)    
        return bstree 

    def get_names(self):
        names = []

        if self.left != None:
            names = names + self.left.get_names()
        names = names + [self.name]
        if self.right != None:
            names = names + self.right.get_names()

        return names
