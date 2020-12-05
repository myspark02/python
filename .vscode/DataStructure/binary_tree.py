class BinarySearchTreeNode :
    def __init__(self, data) :
        self.data = data
        self.left = None
        self.right = None

    
    def addNode(self, data) :
        if (self.data == data) :
            return
        
        if data < self.data :
            if self.left :
                self.left.addNode(data)
            else :
                self.left = BinarySearchTreeNode(data)

        else :
            if self.right :
                self.right.addNode(data)
            else :
                self.right = BinarySearchTreeNode(data)

    def delete(self, data) :
        if data < self.data :
            if self.left :
                self.left = self.left.delete(data)
        
        elif data > self.data :
            if self.right :
                self.right = self.right.delete(data)

        else : # this node is to be deleted
            if self.left is None and self.right is None : # no children then, just deleted
                return None
            elif  self.left is None : #only has a right child 
                return self.right # let parent point to my right child rather than me.. 
            elif self.right is None : # only has a left child
                return self.left # let parent point to my left child
            else : # has both left and right child
                # replace me with my right subtree's min value and then delete the node with min value
                min = self.right.find_min()
                self.data = min
                self.right = self.right.delete(min)

        return self # let parent point me which is got renewed.

    def search(self, data) :
        if self.data == data :
            return True

        if data < self.data :
            if self.left :
                return self.left.search(data)
            else :
                return False
        else :
            if self.right:
                return self.right.search(data)
            else :
                return False


    def in_order_traversal(self) :
        elements = []

        if self.left :
            elements += self.left.in_order_traversal()
        
        elements.append(self.data)

        if self.right :
            elements += self.right.in_order_traversal()

        return elements

    def find_min(self) : 
        if self.left :
            return self.left.find_min()
        else :
            return self.data

    def find_max(self):
        if self.right :
            return self.right.find_max()
        else :
            return self.data

    def post_order_traversal(self) :
        elements = []
        if self.left :
            elements += self.left.post_order_traversal()
        
        if self.right :
            elements += self.right.post_order_traversal()

        elements.append(self.data)

        return elements

    def pre_order_traversal(self) :
        elements = []

        elements.append(self.data)

        if self.left :
            elements += self.left.pre_order_traversal()

        if self.right :
            elements += self.right.pre_order_traversal()

        return elements

    def sum(self) :
        left_sum = self.left.sum() if self.left else 0
        right_sum = self.right.sum() if self.right else 0
        return self.data + left_sum + right_sum
        
def build_tree(elements) :
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)) :
        root.addNode(elements[i])
    
    return root


if __name__ == '__main__':
    numbers = [17, 4, 1, 20, 9, 23, 18, 34, 118, 4]
    numbers_tree = build_tree(numbers)
    print(numbers_tree.in_order_traversal())
    print(numbers_tree.pre_order_traversal())
    print(numbers_tree.post_order_traversal())
    print(numbers_tree.find_max())
    print(numbers_tree.find_min())
    print(numbers_tree.sum())
    print(numbers_tree.search(20))
    numbers_tree.delete(20)
    print(numbers_tree.search(20))
    print(numbers_tree.in_order_traversal())


    countries = ["Korea", "Japan", "China", "UK", "US", "Germany", "France", "UK"]
    country_tree = build_tree(countries)
    print(country_tree.in_order_traversal())
    print("Korea is in the list?", country_tree.search("Korea"))
    print("Sweden is in the list?", country_tree.search("Sweden"))
    
    




        