#!/usr/bin/env python
# coding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12950

# 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다. 2개의 행렬 arr1과 arr2를 입력받아, 행렬 덧셈의 결과를 반환하는 함수, solution을 완성해주세요.
# 
# - 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.

# In[ ]:


arr1= [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
# [[4,6],[7,9]]


# In[ ]:


answer = []


# In[ ]:


for array1, array2 in zip(arr1, arr2):
    inner = []
    for num1, num2 in zip(array1, array2):
        inner.append(num1+num2)
    answer.append(inner)


# In[ ]:


answer


# solution

# In[ ]:


def solution(arr1, arr2):
    answer = []
    
    for array1, array2 in zip(arr1, arr2):
        inner = []
        for num1, num2 in zip(array1, array2):
            inner.append(num1+num2)
        answer.append(inner)
    return answer


# 다른 사람 코드 비슷한데 포문말고 그냥 zip써서 한줄로...

# In[ ]:


answer = [[num1+num2 for num1, num2 in zip(array1, array2)] for array1, array2 in zip(arr1, arr2)]

