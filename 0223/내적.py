#!/usr/bin/env python
# coding: utf-8

# In[10]:


a=[1,2,3,4]
b=[-3,-1,0,2]


# In[11]:


answer = 0


# In[14]:


for idx,v in enumerate(a):
    answer += v*b[idx]


# In[15]:


answer


# solution

# In[ ]:


def solution(a, b):
    answer = 0
    for idx, v in enumerate(a):
        answer += v * b[idx]
    return answer

