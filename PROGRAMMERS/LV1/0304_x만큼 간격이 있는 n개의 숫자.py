#!/usr/bin/env python
# coding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12954

# 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다. 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.
# 
# - x는 -10000000 이상, 10000000 이하인 정수입니다.
# - n은 1000 이하인 자연수입니다.

# In[6]:


x = 2
n = 5
# answer = [2,4,6,8,10]


# In[7]:


answer = list(map(lambda a: a*x, range(1,n+1)))


# In[8]:


answer


# In[ ]:




