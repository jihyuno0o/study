#!/usr/bin/env python
# coding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12940

# 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요. 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다. 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야 합니다.
# 
# - 두 수는 1이상 1000000이하의 자연수입니다.

# In[44]:


n = 2
m = 5
# [3, 12]


# In[45]:


answer = []


# In[46]:


if n > m:
    n, m = m, n


# In[47]:


for a in range(n):
    chek = n-a
    if m%chek == 0 and n%chek == 0:
        answer.append(chek)
        break


# In[48]:


if m % n == 0:
    answer.append(m)
else:
    check = 2
    while(1):
        if n*check % m == 0:
            answer.append(n*check)
            break
        check += 1


# In[49]:


answer


# solution

# In[ ]:


def solution(n, m):
    answer = []
    if n > m:
        n, m = m, n
    
    for a in range(n):
        chek = n-a
        if m%chek == 0 and n%chek == 0:
            answer.append(chek)
            break
    
    if m%n == 0:
        answer.append(m)
    else:
        check = 2
        while(1):
            if n*check % m == 0:
                answer.append(n*check)
                break
            check += 1
            
    return answer


# 다른사람코드

# In[ ]:


def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer


# In[ ]:


def solution(n, m):
    gcd = lambda a,b : b if not a%b else gcd(b, a%b)
    lcm = lambda a,b : a*b//gcd(a,b)
    return [gcd(n, m), lcm(n, m)]

