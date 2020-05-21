#!/usr/bin/env python
# coding: utf-8

# In[ ]:


t=int(input())
for i in range (t): 
    count=0   
    n=int(input())    
    a=list(map(int, input().split()))    
    b=list(map(int, input().split()))    
    a.sort(reverse=True)
    b.sort(reverse=True)
    p=0
    for i in range(n):
        for j in range(p,n):
            if(a[i]>b[j]):
                p=j+1
                count+=1
                break
    print(count)
    


# In[ ]:




