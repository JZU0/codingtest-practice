def solution(arr):
    result = [0, 0] 
    
    def compress(x, y, size):
        first_value = arr[x][y]
        all_same = True
        
        for i in range(x, x + size):
            for j in range(y, y + size):
                if arr[i][j] != first_value:
                    all_same = False
                    break
            if not all_same:
                break

        if all_same:
            result[first_value] += 1
        else:
            half = size // 2
            compress(x, y, half)               
            compress(x, y + half, half)        
            compress(x + half, y, half)        
            compress(x + half, y + half, half) 
            
    compress(0, 0, len(arr))
    
    return result