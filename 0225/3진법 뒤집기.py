#!/usr/bin/env python
# coding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/68935

# 자연수 n이 매개변수로 주어집니다. n을 3진법 상에서 앞뒤로 뒤집은 후, 이를 다시 10진법으로 표현한 수를 return 하도록 solution 함수를 완성해주세요.
# 
# - n은 1 이상 100,000,000 이하인 자연수입니다.

# - n (10진법)  45
# - n (3진법)  1200
# - 앞뒤 반전(3진법)  0021	
# - 10진법으로 표현  7

# In[21]:


n = 45
answer = 0


# In[19]:


arr = []


# In[20]:


while n != 0:
    arr.append(n%3)
    n = n//3


# In[23]:


for i in range(len(arr)):
    answer += 3**i * arr.pop()  
    


# solution

# In[ ]:


def solution(n):
    answer = 0
    arr = []
    while n != 0:
        arr.append(n%3)
        n = n//3
    
    for i in range(len(arr)):
        answer += 3**i * arr.pop()
        
    return answer


# 다른 사람 코드

# In[ ]:


def solution(n):
    tmp = ''
    while n:
        tmp += str(n % 3)
        n = n // 3

    answer = int(tmp, 3)
    return answer

