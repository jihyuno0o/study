#!/usr/bin/env python
# coding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12917

# 문자열 s에 나타나는 문자를 큰것부터 작은 순으로 정렬해 새로운 문자열을 리턴하는 함수, solution을 완성해주세요.
# s는 영문 대소문자로만 구성되어 있으며, 대문자는 소문자보다 작은 것으로 간주합니다.
# 
# 제한 사항
# - str은 길이 1 이상인 문자열입니다.

# In[1]:


s = "Zbcdefg"
# "gfedcbZ"


# In[9]:


word = sorted(s, reverse=True)


# In[10]:


word


# In[11]:


''.join(arr)


# solution

# In[ ]:


def solution(s):
    return ''.join(sorted(s, reverse=True))

