class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

        
class BinaryTree:
    def __init__(self):
        self.root = None

        
    def insert(self, key):
        if not self.root:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

            
    def _insert_recursive(self, current_node, key):
        if key < current_node.key:
            if current_node.left:
                self._insert_recursive(current_node.left, key)
            else:
                current_node.left = Node(key)
        elif key > current_node.key:
            if current_node.right:
                self._insert_recursive(current_node.right, key)
            else:
                current_node.right = Node(key)

                
    def search(self, key):
        return self._search_recursive(self.root, key)

    
    def _search_recursive(self, current_node, key):
        if not current_node or current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._search_recursive(current_node.left, key)
        else:
            return self._search_recursive(current_node.right, key)

        
    def in_order_traversal(self, node):
        if node:
            self.in_order_traversal(node.left)
            print(node.key)
            self.in_order_traversal(node.right)

            
if __name__ == "__main__":
    tree = BinaryTree()
    tree.insert(8)
    tree.insert(6)
    tree.insert(7)
    tree.insert(5)
    tree.insert(3)
    tree.insert(0)
    tree.insert(9)
            
    
    print("Traverse the tree in order: ")
    tree.in_order_traversal(tree.root)
    
    search = input(f"Pick a number to search for: ")
    try:
        search = int(search)
    except:
        search = 7
        print(f"Ok... you didn't give me a number so let's try with 7")
        
    result = tree.search(search)
    if result:
        print(f"Key {search} found in the tree.")
    else:
        print(f"Key {search} not found in the tree.")
