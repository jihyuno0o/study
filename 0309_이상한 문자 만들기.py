#!/usr/bin/env python
# coding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12930

# 문자열 s는 한 개 이상의 단어로 구성되어 있습니다. 각 단어는 하나 이상의 공백문자로 구분되어 있습니다. 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.
# 
# 제한 사항
# - 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
# - 첫 번째 글자는 0번째 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

# "try hello world"	"TrY HeLlO WoRlD"

# In[2]:


s = "try hello world"


# 1번 시도

# In[ ]:


cnt = 0
for i,v in enumerate(list_s):
    if cnt%2==0:
        list_s[i] = v.upper()
        
    if v == ' ':
        cnt = 0    
    else:
        cnt +=1
    


# In[ ]:


answer = ''.join(list_s)


# In[ ]:


answer


# 2번 시도 - 하나이상의 공백 공백개수가 많을수도있음

# In[ ]:


answer = ""
list_s = s.split(" ")
for string in list_s:
    n = ""
    for i, v in enumerate(string):
        if i%2==0:
            n += v.upper()
        else:
            n += v.lower()
    answer += n + " "   


# In[ ]:


answer[:-1]


# solution

# In[ ]:


def solution(s):
    answer = ""
    list_s = s.split(" ")
    for word in list_s:
        n = ""
        for i,v in enumerate(word):
            if i%2==0:
                n += v.upper()
            else:
                n += v.lower()
        answer += n + " "
    
    return answer[:-1]


# 다른 사람 코드

# In[3]:


answer = " ".join(map(lambda x: "".join([a.lower() if i % 2 else a.upper() for i, a in enumerate(x)]), s.split(" ")))
answer


# In[ ]:




