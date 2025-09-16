from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def reverse_even_levels(root):
    # TODO: Complete this function to reverse node values at every even level
    if not root:
        return None
    
    dq = deque([root])
    level = 0
    while dq:
        sz = len(dq)
        if level %2 ==0:
            for x in range(len(dq)//2):
                dq[x].val , dq[len(dq)-1 - x].val = dq[len(dq)-1 - x].val, dq[x].val

        while sz:
            node = dq.popleft()
            if node.left:
                dq.append(node.left)
            if node.right:
                dq.append(node.right)
            sz -= 1
        level+=1    
    return root

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
    print(result)

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
