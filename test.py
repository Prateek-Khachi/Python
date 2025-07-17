from collections import Counter
import heapq

# lst = [1,1,1,2,2,3]
# print(f"This is the {Counter(lst)} map.")

# mpp = {1: 3, 2: 2, 3: 1}
# print(f"This is the {mpp} map.")


# lidt = [7, 2, 23, 4, 57]

# lidt = [-x for x in lidt]
# print(lidt)
# heapq.heapify(lidt)
# print(lidt)
# heapq.heappush(lidt, -1)
# print(lidt)
# lidt = [-x for x in lidt]
# print(lidt)

# matrix = [[1, 2], [3, 4], [5, 6]]

# for i, j in matrix:
#     print(i, j)

# ans = "hello"
# rev = reversed(ans)
# print(rev)  # Output: <reversed object at 0x...>

# h = [0,1,0,2,1,0,1,3,2,1,2,1]
# ans = 0
# l = 0
# r = len(h)-1

# while l<len(h):
            
#     while h[r] < h[l]  and r<len(h):
#         r+=1

#     res = min(h[l], h[r]) * r-l
#     l+=1

#     while(l<r):
                
#         res-= h[l]
#         l+=1
            
#     r=+1
#     ans+=res
#     res=0
        
# print(ans)

# a = [1,2,3,4]
# b = a

# b[0] = 5
# print(a)  # Output: [5, 2, 3, 4]

# from collections import OrderedDict

# od = OrderedDict()
# od[1] = 'A'
# od[2] = 'B'
# od[3] = 'C'

# print(od)  # Output: OrderedDict([(1, 'A'), (2, 'B'), (3, 'C')])

# # Access key 2
# od.move_to_end(2)
# print(od)  # Output: OrderedDict([(1, 'A'), (3, 'C'), (2, 'B')])

# # Remove least recently used (first item)
# od.popitem()
# print(od)  # Output: OrderedDict([(3, 'C'), (2, 'B')])

a ="10"
b="20"
c=a+b
print((c))