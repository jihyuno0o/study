#!/usr/bin/env python
# coding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/77884

# 두 정수 left와 right가 매개변수로 주어집니다. left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.
# 
# - 1 ≤ left ≤ right ≤ 1,000

# In[1]:


left = 13
right = 17
answer = 0


# In[2]:


while left <= right:
    #약수 구하기
    array =[]
    for i in range(left):
        if left%(i+1) == 0:
            array.append(i+1)
    
    if len(array)%2==0:
        answer+=left
    elif len(array)%2!=0:
        answer-=left
    
    left+=1


# solution

# In[ ]:


def solution(left, right):
    answer = 0
    while left <= right:
        #약수 구하기
        array =[]
        for i in range(left):
            if left%(i+1) == 0:
                array.append(i+1)

        if len(array)%2==0:
            answer+=left
        elif len(array)%2!=0:
            answer-=left

        left+=1
        
    return answer


# 다른 사람 코드 보고 배운점 : 제곱수는 약수가 홀수임

# In[ ]:


def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if int(i**0.5) == i**0.5:
            answer -= i
        else:
            answer += i
            
    return answer

