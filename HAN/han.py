import sys                                                                      
from collections import deque                                                   
input = sys.stdin.readline                                                      
                                                                                
n, m = map(int, input().split())                                                
stacks = []                                                                     

                                                                                
for _ in range(m):                                                              
    data = list(map(int, input().split()))                                      
    stacks.append(deque(data[1:]))                                              
                                                                                
for i in range(m):                                                              
    if len(stacks[i]) == n:                                                     
        print(0)                                                                
        sys.exit(0)                                                             
                                                                                
buf = -1                                                                        

for i in range(m):                                                              
    if len(stacks[i]) == 0:                                                     
        buf = i                                                                 

        break                                                                   
                                                                                
if buf == -1:                                                                   

    print(-1)                                                                   
    sys.exit(0)                                                                 
                                                                                
pos = {}                                                                        
for i in range(m):                                                              
    for x in stacks[i]:                                                         
        pos[x] = i                                                              
                                                                                
moves = []                                                                      
for x in range(1, n+1):                                                         
    i = pos[x]                                                                  
    if stacks[i][0] != x:                                                       

        print(-1)                                                               
        sys.exit(0)                                                             
    stacks[i].popleft()                                                         
    stacks[buf].append(x)                                                       

    moves.append((i+1, buf+1))                                                  

                                                                                
print(len(moves))                                                               
for a, b in moves:                                                              
    print(a, b)          