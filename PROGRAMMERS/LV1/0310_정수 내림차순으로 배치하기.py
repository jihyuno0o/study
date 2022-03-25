#!/usr/bin/env python
# coding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12933

# 문제 설명
# 함수 solution은 정수 n을 매개변수로 입력받습니다. n의 각 자릿수를 큰것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요. 예를들어 n이 118372면 873211을 리턴하면 됩니다.
# 
# 제한 조건
# - n은 1이상 8000000000 이하인 자연수입니다.

# In[7]:


n= 118372
# 873211


# In[ ]:


arr = list(str(n))


# In[ ]:


sort = sorted(arr, reverse=True)


# In[ ]:


sort


# In[2]:


answer = int(''.join(sorted(list(str(n)), reverse=True)))
# 2,3,11 런타임 에러


# In[6]:


answer


# In[5]:


answer = int(''.join(sorted(list(str(int(n))), reverse=True)))


# In[8]:


#sorted는 list로 안감싸도 된다?
answer = sorted(str(n))
answer


# 다른 사람 풀이

# In[ ]:



def solution(n):
    ls = list(str(n))
    ls.sort(reverse = True)
    return int("".join(ls))

