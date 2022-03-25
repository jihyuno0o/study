#!/usr/bin/env python
# coding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12903

# 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요. 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.
# 
# 재한사항
# - s는 길이가 1 이상, 100이하인 스트링입니다.

# "abcde"	"c"
# 
# "qwer"	"we"

# In[ ]:


s = "abcde"
s1 = "qwer"


# In[ ]:


(len(s1)/2) % 1.0 != 0


# In[ ]:


length = len(s1)//2
length


# In[ ]:


s1[length] if (len(s1)/2) % 1.0 != 0 else s1[length-1:length+1]


# In[ ]:


s1[1:3]


# solution

# In[ ]:


def solution(s):
    length = len(s)//2
    
    return s[length] if (len(s)/2) % 1.0 != 0 else s[length-1:length+1]

