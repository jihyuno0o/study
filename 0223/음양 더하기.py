#!/usr/bin/env python
# coding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/76501
# 
# 어떤 정수들이 있습니다. 이 정수들의 절댓값을 차례대로 담은 정수 배열 absolutes와 이 정수들의 부호를 차례대로 담은 불리언 배열 signs가 매개변수로 주어집니다. 실제 정수들의 합을 구하여 return 하도록 solution 함수를 완성해주세요.
# 
# -absolutes의 길이는 1 이상 1,000 이하입니다.
#     
#     absolutes의 모든 수는 각각 1 이상 1,000 이하입니다.
# 
# -signs의 길이는 absolutes의 길이와 같습니다.
#     
#     signs[i] 가 참이면 absolutes[i] 의 실제 정수가 양수임을, 그렇지 않으면 음수임을 의미합니다.

# In[9]:


absolutes = [4,7,12]
signs = ['true','false','true']


# In[10]:


answer = 0


# In[11]:


for idx, v in enumerate(signs):
    if v == 'true':
        answer += absolutes[idx]
    elif v == 'false':
        answer -= absolutes[idx]
    print(answer)


# In[12]:


answer


# solution

# In[ ]:


def solution(absolutes, signs):
    answer = 0
    for idx, v in enumerate(signs):
        if v == True:
            answer += absolutes[idx]
        elif v == False:
            answer -= absolutes[idx]
    return answer

