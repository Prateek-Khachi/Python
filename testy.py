for _ in range(1):
        A = [9,7,9]
        B = [7,9,7]
                
        A.sort()
        B.sort()
        
        leftA, rightA = 0, 3 - 1
        leftB, rightB = 0, 3 - 1
        score = 0
        
        while leftA <= rightA and leftB <= rightB:
            if A[rightA] != B[leftB]:
                score += A[rightA] + B[leftB]
                rightA -= 1
                leftB += 1
            elif A[leftA] != B[rightB]:
                score += A[leftA] + B[rightB]
                leftA += 1
                rightB -= 1
            else:
                break
        
        print(score)