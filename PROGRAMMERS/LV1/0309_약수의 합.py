#!/usr/bin/env python
# coding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12928

# 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.
# 
# 제한 사항
# - n은 0 이상 3000이하인 정수입니다.

# 12	28
# 
# 5	6

# In[12]:


n = 12


# In[13]:


sum(a+1 for a in range(n) if n%(a+1)==0)


# In[11]:


for a in range(n):
    if n%(a+1)==0:
        print(a+1)


# 다른 사람 코드

# In[ ]:


def sumDivisor(num):
    # num / 2 의 수들만 검사하면 성능 약 2배 향상잼
    return num + sum([i for i in range(1, (num // 2) + 1) if num % i == 0])

