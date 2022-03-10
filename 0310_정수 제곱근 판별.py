#!/usr/bin/env python
# coding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12934

# 문제 설명
# 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판단하려 합니다.
# n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.
# 
# 제한 사항
# - n은 1이상, 50000000000000 이하인 양의 정수입니다.

# n	return
# 
# 121	144
# 
# 3	-1
# 
# 입출력 예#1
# 121은 양의 정수 11의 제곱이므로, (11+1)를 제곱한 144를 리턴합니다.
# 
# 입출력 예#2
# 3은 양의 정수의 제곱이 아니므로, -1을 리턴합니다.

# In[7]:


n = 121


# In[6]:


import math

r = int(math.sqrt(n))
if r*r == n:
    return (r+1)*(r+1)
else:
    return -1


# In[11]:


sqrt = n**(1/2)
sqrt % 1


# solution

# In[ ]:


import math

def solution(n):
    r = int(math.sqrt(n))
    if r*r == n:
        return (r+1)*(r+1)
    else:
        return -1


# 다른 사람 코드

# In[ ]:


def nextSqure(n):
    sqrt = n ** (1/2)

    if sqrt % 1 == 0:
        return (sqrt + 1) ** 2
    return -1

