#!/usr/bin/env python
# coding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12948

# 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
# 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.
# 
# - s는 길이 4 이상, 20이하인 문자열입니다.

# In[1]:


phone_number = "01033334444"
# "*******4444"


# In[2]:


len(phone_number)


# In[9]:


phone_number[len(phone_number)-4:]


# In[11]:


starcnt = len(phone_number)-4
answer = '*' * starcnt + phone_number[starcnt:]
answer


# solution

# In[ ]:


def solution(phone_number):
    starcnt = len(phone_number)-4
    answer = '*' * starcnt + phone_number[starcnt:]
    return answer

