def dfs(order, length, start, path, combos):
    if len(path) == length:
        combos.append(''.join(path))
        return
    
    for i in range(start, len(order)):
        dfs(order, length, i + 1, path + [order[i]], combos)

def solution(orders, course):
    result = []
    
    for c in course:
        combo_counts = {}  
        
        for order in orders:
            sorted_order = sorted(order)  
            combos = []  
            dfs(sorted_order, c, 0, [], combos)  
            
            for combo in combos:
                if combo in combo_counts:
                    combo_counts[combo] += 1
                else:
                    combo_counts[combo] = 1
        
        max_count = 0
        for count in combo_counts.values():
            if count >= 2:
                max_count = max(max_count, count)
        
        for combo, count in combo_counts.items():
            if count == max_count:
                result.append(combo)
    
    return sorted(result)
