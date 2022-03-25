#!/usr/bin/env python
# coding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12947

# 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다. 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.
# 
# - x는 1 이상, 10000 이하인 정수입니다.

# 10	true
# 12	true
# 11	false
# 13	false

# In[14]:


x = 11


# In[15]:


arr = list(str(x))
arr


# In[16]:


if x % sum(list(map(int, arr))) != 0:
    answer = False


# In[17]:


answer


# solution

# In[ ]:


def solution(x):
    answer = True
    arr = list(str(x))
    
    if x % sum(list(map(int, arr))) != 0:
        answer = False
    return answer


# 다른 사람 풀이

# In[18]:


11 % sum([int(c) for c in str(11)]) == 0


# In[ ]:




