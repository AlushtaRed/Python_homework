# import os
s = 6
p = 9
# solutions = []
for i in range(1,1001):
    
    for j in range(1,1001):
        if s == i + j and p == i*j:
            
            if i <=j:
                
                
                print(i,j)
                
