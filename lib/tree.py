class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, id):
        def traverse(node):
            if not node:
                return None
            if node.get('id') == id:
                return node
            for child in node.get('children', []):
                result = traverse(child)
                if result:
                    return result
            return None

        return traverse(self.root)
