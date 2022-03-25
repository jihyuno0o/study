#!/usr/bin/env python
# coding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12931

# 문제 설명
# 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# 예를들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.
# 
# 제한사항
# - N의 범위 : 100,000,000 이하의 자연수

# N	answer
# 
# 123	6
# 
# 987	24

# In[1]:


n = 123


# In[2]:


answer = sum(list(map(int, list(str(n)))))


# In[3]:


answer


# 다른 사람 코드

# In[ ]:


def sum_digit(number):
    return sum([int(i) for i in str(number)])


# In[4]:


for i in str(n):
    print(i)


# In[ ]:




