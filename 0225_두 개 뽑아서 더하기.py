#!/usr/bin/env python
# coding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/68644

# 정수 배열 numbers가 주어집니다. numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.
# 
# - numbers의 길이는 2 이상 100 이하입니다.
#     - numbers의 모든 수는 0 이상 100 이하입니다.

# In[10]:


numbers = [2,1,3,4,1]
answer = []


# In[11]:


numbers.sort()
numbers


# In[9]:


a = -1
for i in range(len(numbers)):
    b = numbers.pop()
    if a != b:
        a = b
        for v in numbers:
            answer.append(a+v)
            print(answer) 
    else:
        continue
       


# In[12]:


for i in range(len(numbers)):
    a = numbers.pop()
    for v in numbers:
        answer.append(a+v)
        print(answer) 


# solution

# In[ ]:


def solution(numbers):
    answer = []
    for i in range(len(numbers)):
        a = numbers.pop()
        for v in numbers:
            answer.append(a+v)
    
    answer = set(answer)
    return sorted(list(answer))

