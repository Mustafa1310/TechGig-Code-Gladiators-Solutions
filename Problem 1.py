#!/usr/bin/env python
# coding: utf-8

# In[ ]:


''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    n=int(input())
    l=list(map(int,input().split()))
    m=list(map(int,input().split()))
    z=[]
    for i in range(n):
        z.append(int(m[i]//l[i]))
    print(min(z))    


main()


# In[ ]:




