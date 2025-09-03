from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def reverse_even_levels(root):
    # TODO: Complete this function to reverse node values at every even level
    return root

# Helper function to print the tree in level order
def print_level_order(root):
    if not root:
        return []
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.val)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
        print(x.val for x in queue)

# Example usage
if __name__ == "__main__":
    # Construct tree:      1
    #                   /    \
    #                  2      3
    #                 / \    / \
    #                4  5   6   7
    root = TreeNode(1)
    root.left = TreeNode(2, TreeNode(4), TreeNode(5))
    root.right = TreeNode(3, TreeNode(6), TreeNode(7))
    
    print("Before:")
    print_level_order(root)
    root = reverse_even_levels(root)
    print("After:")
    print_level_order(root)
