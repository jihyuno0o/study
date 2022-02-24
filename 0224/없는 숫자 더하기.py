#!/usr/bin/env python
# coding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/86051

# 0부터 9까지의 숫자 중 일부가 들어있는 정수 배열 numbers가 매개변수로 주어집니다. numbers에서 찾을 수 없는 0부터 9까지의 숫자를 모두 찾아 더한 수를 return 하도록 solution 함수를 완성해주세요.
# 
# - 1 ≤ numbers의 길이 ≤ 9
#     - 0 ≤ numbers의 모든 원소 ≤ 9
#     - numbers의 모든 원소는 서로 다릅니다.

# In[12]:


numbers = [1,2,3,4,6,7,8,0]
check = [0,1,2,3,4,5,6,7,8,9]


# In[14]:


for v in numbers:
    check.remove(v)

sum(check)


# solution

# In[ ]:


def solution(numbers):
    answer = -1
    check=[0,1,2,3,4,5,6,7,8,9]
    
    for v in numbers:
        check.remove(v)
        
    return sum(check)


# 다른 사람 코드.. 미쳤나

# In[ ]:


def solution(numbers):
    return 45 - sum(numbers)

