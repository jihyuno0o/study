# studyPython


## 소수 확인하기

```
def isitPrime(k):
    if k==2 or k==3: return True
    if k%2==0 or k<2: return False
    for i in range(3, int(k**0.5)+1, 2):
        if k%i==0:
            return False

    return True
print(isitPrime(13))
```

2부터 +1 하면서 확인하는 방법보다 30% 더 빠르고 효율적

#### sympy.isprime() 함수
```
from sympy import *
  
isprime(8)
isprime(11)
```


## 리스트 콤비네이션

```
for i in range(len(nums)-2):
    one = nums[i]
    for j in range(i+1, len(nums)-1):
        two = nums[j]
        for k in range(j+1, len(nums)):
            three = nums[k]
            print(one+two+three)
```
이렇게 3개 콤비 구하려면 for문을 3중으로 써야하는데

#### itertools.combinations() 
```
from itertools import combinations
for a in combinations(nums, 3):
    print(a)
```


## 최대공약수 최소공배수

- 최대공약수 : Greatest Common Measure
- 최소공배수 : Least Common Multiple

    - A와 B의 자연수
    - 최대 공약수 = G
    - 최소 공배수 L = G x a x b 
    - A x B = G x L = G x a x b x G

```
# 최대공약수
import math
G = math.gcd(A, B)

# 최소공배수
L = A * B // G
```


## 피보나치 수

F(n) = F(n-1) + F(n-2)
* F(0) = 0, F(1) = 1
* F(2) = F(1) + F(0) = 1 + 0 = 1
* F(3) = F(2) + F(1) = 1 + 1 = 2
* F(4) = F(3) + F(2) = 2 + 1 = 3
* ...
 
#### 재귀를 이용한 코드
```
def fibo(n):
    if n == 0:
        return 0
    elif n ==1 or n==2:
        return 1
    else:
        return fibo(n-2) + fibo(n-1)
```

#### 재귀 + DP
```
def fibo(f, n):
    if f[n] != -1:
        return f[n]
    else:
        f[n] = fibo(f, n-1) + fibo(f, n-2)
        return f[n]

def solution(n):
    
    f = [-1] * (n+1)
    f[0], f[1] = 0, 1

    return fibo(f, n)
```

## 2진수, 8진수, 16 진수

- 2진수 : 0b
- 8진수 : 0o
- 16진수 : 0x

#### bin(),oct(), hex()
```
# 접두어 포함
bin(42)
oct(42)
hex(42)

bin(0b101010) #'0b101010'
oct(0b101010) #'0o52'
hex(0b101010) #'0x2a'
str(0b101010) #'42'
```

#### int()
```
int('0b101010', 2)
int('0o52', 8)
int('ox2a', 16)
```
int() 는 base 는 디폴트 갑이 10
```
int('42', 10)
int('42')
```

#### fotmat()
```
# 접두어 없이 나옴
format(42, 'b')
format(42, 'o')
format(42, 'x')
format(42, 'd')

# 접두어 포함
format(42, '#b')
format(42, '#o')
format(42, '#x')
```

## 양의 무한대(inf), 음의 무한대(-inf)

#### 최대값, 최소값 구할때 유용한 float('inf')
float형에만 적용가능 (int형에 적용불가)
```
max = float('inf')
min = float('inf')
```

#### Mathematical Function (Python 3.5이상)
```
import math

max = math.inf
min = -math.inf
```

###### 프로그래머스 - 교점에 별 만들기
처음에 x,y 각각의 최소, 최대값을 -1000 정도로 생각했는데 min, max가 너무 작아서 실패로 뜨나 싶어서 찾아봄
```
INF = float('inf')
minx, maxx, miny, maxy = INF, -INF, INF, -INF
```

## 데크(deque)
큐(queue)는 선입선출(FIFO)지만, 데큐(deque)는 양방향 큐로 앞, 뒤로 추가나 제거가 가능
- 양끝의 추가와 제거가 리스트보다 훨씬 빠름 
- 리스트는 O(n), 데큐는 O(1)

#### collections.deque
```
from collections import deque

deq = deque() 
deq.appendleft(1) # deque([1])
deq.append(-1) # deque([1, -1])
deq.popleft() # 1
deq.pop() # -1
```

이외에도 deque.remove(item)이나 deque.rotate(num)-데크를 num만큼 회전(양수면 오른쪽, 음수면 왼쪽)-등 유용한 메서드가 있음

## 2차원 리스트를 1차원 리스트로 만들기
- for loop 와 List comprehension
- sum()
- itertools

#### for loop 와 List comprehension
for loop
```
list1 = [[1,10], [2,20], [3,30], [4,40]]
list2 = []
for inner_list in list1:
    for data in inner_list:
        list2.append(data)
print(list2)
```

list comprehension
```
list1 = [[1,10], [2,20], [3,30], [4,40]]
list2 = [data for inner_list in list1 for data in inner_list]
print(list2)
```

#### sum()
sum(iterable, start) : start에 iterable의 데이터를 더하는 함수
```
list1 = [[1,10], [2,20], [3,30], [4,40]]
list2 = sum(list1, [])
# [] + [1,10] + [2,20] + [3,30] + [4,40] 연산 수행
# python 에서 [1,10] + [2,20] 은 [1,10,2,20]
print(list2)
```

#### itertools.chain() 
```
import itertools

list1 = [[1,10], [2,20], [3,30], [4,40]]
list2 = list(itertools.chain(*list1))
# 언패킹 해서 1차원으로 만들고, 그 안의 데이터를 연결. 전체를 list로 다시 묶음
print(list2)
```
