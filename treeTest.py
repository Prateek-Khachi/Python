from typing import Optional
import collections

class TreeNode:
    def __init__ (self, val : int = 0 , left: Optional['TreeNode'] =None , right:Optional['TreeNode'] = None):
        self.val = val
        self.left = left
        self.right = right


def create_tree_from_list(values: list) -> Optional[TreeNode]:
    if not values:
        return None
    
    root = TreeNode(values[0])
    queue = collections.deque([root])
    index = 1

    while queue and index < len(values):
        curr = queue.popleft()

        if values[index]:
            curr.left =TreeNode(values[index])
            queue.append(curr.left)

        index += 1

        if index < len(values) and values[index]:
            curr.right = TreeNode(values[index])
            queue.append(curr.right)

        index += 1

    return root

def bfs(root: Optional[TreeNode]) -> None:
    if not root:
        return
    
    queue = collections.deque([root])
    level = 1

    while queue:
        size = len(queue)
        print(f"Level {level}: ", end="")
        for x in range(size):
            print(queue[x].val, end=" ")
        print()

        while size > 0:
         
            curr = queue.popleft()
            
            if curr.left:
                queue.append(curr.left)
            if curr.right:  
                queue.append(curr.right)   

            size-=1    
        level += 1


list_of_values = [1, 2, 3, 4, 5, 6]
tree = create_tree_from_list(list_of_values)    

bfs(tree)          

