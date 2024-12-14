class Tree:
    def __init__(self, root=None):
        self.root = root

    def get_element_by_id(self, target_id):
        # Helper function for DFS traversal
        def dfs(node):
            # If the current node's id matches the target id, return the node
            if node['id'] == target_id:
                return node
            
            # Otherwise, recursively search the children
            for child in node['children']:
                result = dfs(child)
                if result:
                    return result
            return None

        # Start DFS from the root of the tree
        if self.root:
            return dfs(self.root)
        return None
