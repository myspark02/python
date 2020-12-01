class TreeNode:
    def __init__(self, data) :
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child) :
        child.parent = self
        self.children.append(child)

    def get_level(self) :
        level = 0
        p = self.parent

        while p :
            p = p.parent
            level += 1

        return level

    def print_tree(self) :
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""

        print(prefix + self.data)    

        for child in self.children:
            child.print_tree()

    def print_tree(self, which) :
        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""

        if which == 'name':
            print(prefix + self.data[1])
        elif which == 'designation':
            print(prefix + self.data[0])    
        else:
            print(prefix + self.data[1] + ' (' + self.data[0]+')')    

        for child in self.children:
            child.print_tree(which)    

    def print_tree(self, level) :
        if self.get_level() > level :
            return

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""

        print(prefix + self.data)    

        for child in self.children:
            child.print_tree(level)                
        

def build_product_tree() :
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode('Mac'))
    laptop.add_child(TreeNode('Surface'))
    laptop.add_child(TreeNode('Thinkpad'))

    cellphone = TreeNode('Cell Phone')
    cellphone.add_child(TreeNode('iPhone'))
    cellphone.add_child(TreeNode('Galaxy'))
    cellphone.add_child(TreeNode('Optimus'))

    tv = TreeNode('TV')
    tv.add_child(TreeNode('Samsung'))
    tv.add_child(TreeNode('LG'))

    root.add_child(laptop)
    root.add_child(cellphone)
    root.add_child(tv)

    return root


def build_product_tree2() :
    ceo = TreeNode(('CEO', 'Nilson'))

    cto = TreeNode(('CTO', 'Charles'))
    ih = TreeNode(('Infrastructure Head', 'James'))
    cm = TreeNode(('Cloud Manager', 'Victoria'))
    am = TreeNode(('App Manger', 'David'))
    ah = TreeNode(('Application Head', 'Amanda'))
    
    ih.add_child(cm)
    ih.add_child(am)

    hrh = TreeNode(('HR Head', 'Gales'))
    rm = TreeNode(('Recruitment Manager', 'Peter'))
    pm = TreeNode(('Policy Manager', 'Watson'))
    
    cto.add_child(ih)
    cto.add_child(ah)

    hrh.add_child(rm)
    hrh.add_child(pm)

    ceo.add_child(cto)
    ceo.add_child(hrh)

    return ceo

if __name__ == '__main__' :
    root = build_product_tree()
    root.print_tree(0)

    # root = build_product_tree2()
    # print()
    # root.print_tree('name')
    # print()

    # print()
    # root.print_tree('designation')
    # print()

    # print()
    # root.print_tree('both')
    # print()
