
import re

"""Klasa implementująca strukturę węzła"""

class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None  # lewy potomek
        self.right = None  # prawy potomek


"""Klasa implementująca strukturę BST"""

class BinarySearchTree(object):

    def __init__(self):
        self.root = None
        self.max_numer_of_elements = 0
        self.current_number_of_elements = 0
        self.number_of_loaded_elements = 0
        self.find_compares = 0

    """Metoda przeszukuje drzewo szukając  w nim Node'a o dajnej wartości pola key"""
    """zwraca 1 gdy znajdzie , 0 gdy nie znajdzie"""

    def find(self, key):

        if self.root is None:
            return 0
        node = self.find_node(self.root, key)
        if node is None:
            return 0
        else:
            return 1

    """wstawianie do drzewa wartości kluczowej"""

    def insert(self, key):

        self.current_number_of_elements += 1
        if self.current_number_of_elements > self.max_numer_of_elements:
            self.max_numer_of_elements = self.current_number_of_elements

        self.tree_insert(self.root, key)


    """funkcja wczytująca kilka elementów jednoczenie z pliku"""

    def load(self, name):
        huge_list = []
        huge_list2 = []
        with open(name, "r") as f:
            for line in f:
                huge_list.extend(line.split())
                #usun niepotrzrbne znaki
            for e in huge_list:
                temp = re.sub("[^(a-zA-Z)]", "", e)
                huge_list2.append(temp)

        #zwiększ ilośc elementów dodanych
        self.number_of_loaded_elements += len(huge_list2)
        for e in huge_list2:
            self.insert(str(e))

    """funkcja wskazuje  usuwa wartość kluczową z drzewa"""

    def delete(self, key):

        if self.find(key) == 1:
            self.current_number_of_elements -= 1
        self.root = self.delete_rbt_structure(self.root, key)

    """ funkcja wstawia nowy Node wraz z jego wartością- key"""

    def tree_insert(self, root, key):

        if self.root is None:
            self.root = Node(key)
        else:
            if root.value.lower() < key.lower():
                if root.right is None:
                    root.right = Node(key)
                else:
                    self.tree_insert(root.right, key)
            else:
                if root.left is None:
                    root.left = Node(key)
                else:

                    self.tree_insert(root.left, key)




    """generator przechodzący po BST inorder"""
    def tree_inorder(self, root):

        if root is not None:
            yield from self.tree_inorder(root.left) if root.left is not None else ()
            yield root.value if root.value is not None else ()
            yield from self.tree_inorder(root.right) if root.right is not None else ()

    """funkcja zwracja maksymalną wartość klucza albo pustą linie"""

    def max(self):

        if self.root is None:
            return ""
        node = self.root
        while node.right is not None:
            node = node.right
        return node.value

    """funkcja zwracja minimalną wartość klucza albo pustą linie"""

    def min(self):

        if self.root is None:
            return ""
        node = self.tree_minimum(self.root)
        while node.left is not None:
            node = node.left
        return node.value

    """inorder traversal"""

    def inorder(self):
        tab = list(self.tree_inorder(self.root))
        line = ""
        for v in tab:
            line += v
            line += " "
        return line



    def delete_rbt_structure(self, root, key):

        if root is None:
            return root

        if key.lower() < root.value.lower():
            root.left = self.delete_rbt_structure(root.left, key)

        elif key.lower() > root.value.lower():
            root.right = self.delete_rbt_structure(root.right, key)

        else:

            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp

            temp = self.tree_minimum(root.right)

            root.value = temp.value
            root.right = self.delete_rbt_structure(root.right, temp.value)
        return root

    """funkcja zwraca wartość następnika"""

    def successor(self, key):

        succ = self.tree_successor(self.root, key)
        if succ is None:
            return ""
        else:
            return succ.value

    def tree_successor(self, root, key):


        node = self.find_node(self.root, key)

        if node is None:
            return None

        if node.right is not None:
            return self.tree_minimum(node.right)
        else:
            succ = None
            while root is not None:
                if node.value.lower() < root.value.lower():
                    succ = root
                    root = root.left
                elif node.value.lower() > root.value.lower():
                    root = root.right
                else:
                    break
            return succ

    def tree_minimum(self, root):

        while root.left is not None:
            root = root.left
        return root

    def find_node(self, root, key):

        if root is None:
            return None
        if root.value == key:
            self.find_compares += 1
            return root
        if root.value.lower() < key.lower():
            self.find_compares += 1
            return self.find_node(root.right, key)
        else:
            return self.find_node(root.left, key)



