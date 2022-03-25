#!/usr/bin/env python
# coding: utf-8

# https://programmers.co.kr/learn/courses/30/lessons/12921

# 1부터 입력받은 숫자 n 사이에 있는 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
# 
# 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# (1은 소수가 아닙니다.)
# 
# 제한 조건
# - n은 2이상 1000000이하의 자연수입니다.

# In[ ]:


n = 5
num = [2,3]


# 시간초과 나옴

# In[ ]:


for i in range(4,n+1):
    check = True
    for v in num:
        if i%v == 0:
            check = False
            break
            
    if check == True:
        num.append(i)


# In[ ]:


num


# In[ ]:





# In[8]:


n = 5


# In[9]:


check = [True]*(n+1)
m = int(n**0.5)
check


# In[10]:


for i in range(2, m+1):
    if check[i]==True:
        for j in range(i*i, n+1, i):
            print(j)
            check[j] = False
check


# In[14]:


answer = check.count(True)-2


# In[15]:


answer


# In[ ]:





# 일단 여기서는 간단히 3가지 수학 정리만 소개하겠습니다.
# 
# 1보다 큰 모든 자연수는 소수의 곱으로 이루어져 있다.
# 이것은 가장 기본적인 정리입니다. 이 정리가 의미하는 바는 무엇일까요? 대부분의 사람들은 소수를 구하기 위해서 2부터 차례대로 증가시켜서 나누어보는 방법을 이용할 것 입니다. 그러나 이 방식은 굉장히 비효율적인입니다. 그렇지만 1보다 큰 자연수는 소수의 곱으로 이루어져 있기 때문에 소수로만 나누면 됩니다. 예를 들어서, 10이 소수인지 아닌지를 알기 위해서 10보다 작은 소수만을 이용하면 됩니다. 실제로 10보다 작은 소수는 4개입니다. 그러니깐 4개만 이용하면 됩니다. 그리고 100이 소수인지 아닌지를 알기 위해서 99개의 자연수를 모두 이용한 것 대신에 25개의 소수만 이용하면 됩니다.
# 
# 어떤 자연수 n이 있을 때, √n 보다 작은 모든 소수들로 나누어 떨어지지 않으면 n은 소수입니다.
# 언뜻 이해하기 힘들겠지만 한 번 이해하면 쉽습니다. 증명을 생략하고 예를 들겠습니다. 먼저 101이 소수인지 아닌지 판별하기 위해서 우리는 √101을 구하면 10.xxx이 됩니다. 자 10보다 작은 소수는 뭐가 있을까요? 일단 2, 3, 5, 7이 있습니다. 그런데 딱 봐도 이 4개의 소수로만 101이 나누어 떨어지지 않습니다. 그러므로 101소수입니다. 위의 방식을 이용하면 25개의 소수를 모두 이용해야 하지만 지금은 4개만 이용해도 쉽게 계산이 됩니다.
# 
# 2보다 큰 모든 짝수는 어차피 합성수입니다. 어차피 2로 나누어 떨어지기 때문이죠. 이 방식은 사용하지 않았습니다. 저는 위의 2가지 방식만을 이용해서 효율성 테스트를 통과했습니다.

# 

# solution

# In[ ]:


def solution(n):
    check = [True]*(n+1)
    m = int(n**0.5)
    
    for i in range(2, m+1):
        if check[i] == True:
            for j in range(i*i, n+1, i):
                check[j]=False
    
    return check.count(True) -2


# 다른 사람 코드
# - 에라토스테네스의 체

# In[ ]:


def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            num-=set(range(2*i,n+1,i))
    return len(num)

