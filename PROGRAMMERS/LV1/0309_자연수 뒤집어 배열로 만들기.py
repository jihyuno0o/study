#!/usr/bin/env python
# coding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12932

# 문제 설명
# 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요. 예를들어 n이 12345이면 [5,4,3,2,1]을 리턴합니다.
# 
# 제한 조건
# - n은 10,000,000,000이하인 자연수입니다.

# In[8]:


n = 12345
# [5,4,3,2,1]


# In[7]:


answer = [int(a) for a in list(str(n))]
answer.reverse()
answer


# solution

# In[ ]:


def solution(n):
    answer = [int(a) for a in list(str(n))]
    answer.reverse()
    return answer


# 다른 사람 코드

# In[9]:


answer = list(map(int, reversed(str(n))))
answer


# In[ ]:




