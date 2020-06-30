import sys
import re


class Node():
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left = None
        self.right = None
        self.color = 1




class RBT():
    def __init__(self):
        self.TNULL = Node(0)
        self.TNULL.color = 0
        self.TNULL.left = None
        self.TNULL.right = None
        self.root = self.TNULL
        self.max_numer_of_elements=0
        self.current_number_of_elements =0
        self.number_of_loaded_elements = 0


    def __pre_order_helper(self, node):
        if node != self.TNULL:
            sys.stdout.write(node.data + " ")
            self.__pre_order_helper(node.left)
            self.__pre_order_helper(node.right)

    def __in_order_helper(self, node,list):
        if node != self.TNULL:
            self.__in_order_helper(node.left,list)
            list.append(node.data)
            self.__in_order_helper(node.right,list)

    def __post_order_helper(self, node):
        if node != TNULL:
            self.__post_order_helper(node.left)
            self.__post_order_helper(node.right)
            sys.stdout.write(node.data + " ")

    def __search_tree_helper(self, node, key):
        if node == self.TNULL or str(key).lower() == str(node.data).lower():
            #operujemy na stringach wiec jak zwroci int to znaczyh ze nie ma w drzewie takiego elementu
            if isinstance(node.data,int):
                return 0
            else:
                return 1

        if str(key).lower() < str(node.data).lower():
            return self.__search_tree_helper(node.left, key)
        return self.__search_tree_helper(node.right, key)

    # Balancing the tree after deletion
    def delete_fix(self, x):
        while x != self.root and x.color == 0:
            if x == x.parent.left:
                s = x.parent.right
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.left_rotate(x.parent)
                    s = x.parent.right

                if s.left.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.right.color == 0:
                        s.left.color = 0
                        s.color = 1
                        self.right_rotate(s)
                        s = x.parent.right

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.right.color = 0
                    self.left_rotate(x.parent)
                    x = self.root
            else:
                s = x.parent.left
                if s.color == 1:
                    s.color = 0
                    x.parent.color = 1
                    self.right_rotate(x.parent)
                    s = x.parent.left

                if s.right.color == 0 and s.right.color == 0:
                    s.color = 1
                    x = x.parent
                else:
                    if s.left.color == 0:
                        s.right.color = 0
                        s.color = 1
                        self.left_rotate(s)
                        s = x.parent.left

                    s.color = x.parent.color
                    x.parent.color = 0
                    s.left.color = 0
                    self.right_rotate(x.parent)
                    x = self.root
        x.color = 0

    def __rb_transplant(self, u, v):
        if u.parent == None:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def __delete_node_helper(self, node, key):
        z = self.TNULL
        while node != self.TNULL:
            if node.data == key:
                z = node

            if str(node.data).lower() <= str(key).lower():
                node = node.right
            else:
                node = node.left

        if z == self.TNULL:
            "Couldn't find key in the tree"
            return

        y = z
        y_original_color = y.color
        if z.left == self.TNULL:
            x = z.right
            self.__rb_transplant(z, z.right)
        elif (z.right == self.TNULL):
            x = z.left
            self.__rb_transplant(z, z.left)
        else:
            y = self.minimum(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.__rb_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y

            self.__rb_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == 0:
            self.delete_fix(x)

    # Balance the tree after insertion
    def fix_insert(self, k):
        while k.parent.color == 1:
            if k.parent == k.parent.parent.right:
                u = k.parent.parent.left
                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.left:
                        k = k.parent
                        self.right_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.left_rotate(k.parent.parent)
            else:
                u = k.parent.parent.right

                if u.color == 1:
                    u.color = 0
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    k = k.parent.parent
                else:
                    if k == k.parent.right:
                        k = k.parent
                        self.left_rotate(k)
                    k.parent.color = 0
                    k.parent.parent.color = 1
                    self.right_rotate(k.parent.parent)
            if k == self.root:
                break
        self.root.color = 0

    def __print_helper(self, node, indent, last):
        if node != self.TNULL:
            sys.stdout.write(indent)
            if last:
                sys.stdout.write("R----")
                indent += "     "
            else:
                sys.stdout.write("L----")
                indent += "|    "

            s_color = "RED" if node.color == 1 else "BLACK"
            print(str(node.data) + "(" + s_color + ")")
            self.__print_helper(node.left, indent, False)
            self.__print_helper(node.right, indent, True)

    def preorder(self):
        self.__pre_order_helper(self.root)

    def inorder(self):
        list=[]
        self.__in_order_helper(self.root,list)
        return list

    def postorder(self):
        self.__post_order_helper(self.root)

    def searchTree(self, k):
        return self.__search_tree_helper(self.root, k)

    def minimum(self, node):
        if node == None:
            return "\n"

        while node.left != self.TNULL:
            node = node.left
        return node.data

    def maximum(self, node):
        if node == None:
            return "\n"

        if node.right != None:
            while node.right != self.TNULL:
                node = node.right
            return node.data
        else:
            return "\n"

    def successor(self, value):
        """if x.right != self.TNULL:
            return self.minimum(x.right)

        y = x.parent
        while y != self.TNULL and x == y.right:
            x = y
            y = y.parent
        return y"""
        value = str(value)
        list = self.inorder()

        if value not in list:
            return ""

        for i in range(1, len(list)):
            if list[i - 1] == value and list[i-1] != list[-1]:
                return list[i]
        return ""

    def predecessor(self, x):
        if (x.left != self.TNULL):
            return self.maximum(x.left)

        y = x.parent
        while y != self.TNULL and x == y.left:
            x = y
            y = y.parent

        return y

    def left_rotate(self, x):
        y = x.right
        x.right = y.left
        if y.left != self.TNULL:
            y.left.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def right_rotate(self, x):
        y = x.left
        x.left = y.right
        if y.right != self.TNULL:
            y.right.parent = x

        y.parent = x.parent
        if x.parent == None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert(self, key):
        self.current_number_of_elements += 1
        if self.current_number_of_elements > self.max_numer_of_elements:
            self.max_numer_of_elements =  self.current_number_of_elements

        node = Node(str(key))
        node.parent = None
        node.data = str(key)
        node.left = self.TNULL
        node.right = self.TNULL
        node.color = 1

        y = None
        x = self.root

        while x != self.TNULL:
            y = x
            if str(node.data).lower() < str(x.data).lower():
                x = x.left
            else:
                x = x.right

        node.parent = y
        if y == None:
            self.root = node
        elif str(node.data).lower() < str(y.data).lower():
            y.left = node
        else:
            y.right = node

        if node.parent == None:
            node.color = 0
            return

        if node.parent.parent == None:
            return

        self.fix_insert(node)

    def get_root(self):
        return self.root

    def delete_node(self, data):
        if self.searchTree(data) == 1:
            self.current_number_of_elements -=1
        self.__delete_node_helper(self.root, str(data))

    def print_tree(self):
        self.__print_helper(self.root, "", True)

    def load(self, name):
        huge_list = []
        huge_list2 = []
        with open(name, "r") as f:
            for line in f:
                huge_list.extend(line.split())
                # delete commas ans dots
            for e in huge_list:
                temp = re.sub("[^(a-zA-Z)]", "", e)
                huge_list2.append(temp)

        #incerase number of loaded elements
        self.number_of_loaded_elements += len(huge_list2)
        for e in huge_list2:
            self.insert(str(e))

"""
if __name__ == "__main__":
    bst = RBT()

    bst.insert(55);
    bst.insert(40);
    bst.insert(65);
    bst.insert(60);
    bst.insert(75);
    bst.insert(57);
    bst.insert("a");


    bst.print_tree()

    print("\nAfter deleting an element")
    bst.delete_node(40)
    bst.print_tree()
    bst.inorder()
    print(bst.searchTree("a"))
    print(bst.maximum(bst.get_root()))
    print(bst.minimum(bst.get_root()))
    bst.load("input.txt")
    bst.inorder()
"""