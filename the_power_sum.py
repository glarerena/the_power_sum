def powerSum(X, N):
    
    def helper(total, power, num_present):
        val = total - num_present**power
        
        if val <= 0:
            if val == 0:
                return 1
            return 0
            
        
        
        return helper(val, power, num_present+1) + helper(total, power, num_present+1)
            
        
    return helper(X, N, 1)