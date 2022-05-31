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




## 순열과 조합
itertools를 사용하는 것이 구현하는 것보다 훨씬 빠름 (라이브러리가 빠름)


#### 조합 : itertools.combinations()
- 반복 가능한 객체에 대해 중복을 허용하지 않고 r개를 뽑아서 조합
- 순서는 고려X
- combinations(반복가능객체, r)

```
from itertools import combinations
for i in combinations([0,1,2,3] ,2):
    print(i)
# (0,1), (0,2), (0,3), (1,2), (1,3), (2,3)
```


#### 순열 : itertools.permutations()
- 반복 가능한 객체에 대해 중복을 허용하지 않고 r개를 뽑아서 나열
- 순서 의미O (같은 값이 뽑혀도 순서가 다르면 다른 경우)
- permutations(반복 가능한 객체, r)

```
from itertools import permutations
for i in permutations([0,1,2,3], 2):
    print(i)
# (0,1), (0,2), (0,3), (1,0), (1,2), (1,3), (2,0), (2,1), (2,3), (3,0), (3,1), (3,2)
```




## 최대공약수 최소공배수

- 최대공약수 : Greatest Common Denominator
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




## 소수점 자리수 조절

- 반올림 : round(float, n)
    - 소수점 n자리 까지 표현
    - round(4.3, 0) => 4
    - 소수점이 아닌 정수도 반올림 가능
    - round(12345, -1) => 12340
    
- 올림, 내림 버림 : import math
    - math.ceil(float) : 올림
    - math.floor(float) : 내림
    - math.trunc(float) : 버림




## global, nonlocal 변수


#### 더 넓은 범위에 있는 변수 '읽기'는 가능
```
n = 0 # 전역변수
def func():
    print(n) # 0
func()
```
전역변수는 아니지만 더 넓은 범위의 변수도 가능
```
def func1():
    n = 1
    def func2():
        print(n) # 1
    func2()
func1()
```


#### 더 넓은 범위에 있는 변수 '변경'은 불가능
```
n = 0
def func():
    n += 1 # error
    print(n)
func()

def func1():
    n = 1
    def func2():
        n += 1 # error
        print(n)
    func2()
func1()
```
UnboundLocalError: local variable 'n' referenced before assignment 에러가 발생


#### global
- 전역 변수를 함수 내부에서 변경하고자 할 때, 함수 내의 n이 아닌 전역변수 n을 사용한다는 의미로 global n 선언을 해주어야 함
```
n = 1 # 전역변수
def func1():
    def func2():
        global n
        n += 1
        print(n) # 2
    func2()
func1()
```


#### nonlocal 
- 전역 변수도 아니고 현재 scope 내의 지역변수가 아닌 변수를 사용하고자 할 때는 nonlcoal 키워드를 사용
- 전역 변수가 아니고 지역 변수가 아닌 경우에 global 을 사용하면 NameError: name 'n' is not defined에러가 발생
- 이 경우는 nonlocal n 선언
```
def func1():
    n = 1
    def func2():
        nonlocal n
        n += 1
        print(n) # 2
    func2()
func1()
```




## set (집합)
- s = set([1, 2, 3])
- s = set() # 비어있는 집합
- 중복 허용 X
- 순서 X => 인덱싱 X

```
s1 = set([1, 2, 3, 4, 5])
s2 = set([4, 5, 6, 7, 8])
```


#### 교집합
```
s1 & s2 # {4, 5}

s1.intersections(s2) # {4, 5}
```


#### 합집합
```
s1 | s2 # {1, 2, 3, 4, 5, 6, 7, 8}

s1.union(s2) # {1, 2, 3, 4, 5, 6, 7, 8}
```


#### 차집합
```
s1 - s2 # {1, 2, 3}

s2.difference(s1) # {6, 7, 8}
```


#### set의 다른 메소드
- set.add(10) : 1개의 값 추가
- set.update([10, 11, 12]) : 여러 개의 값 한번에 추가
- set.remove(10) : 특정 값 제거 




## heapq
- 파이썬의 내장모듈
- 이진트리 기반의 최소 힙 자료구조
- 원소들이 항상 정렬된 상태로 추가되고 삭제됨
- 가장 작은 값의 인덱스는 항상 0
- 가장 큰 값은 항상 -1 이 아님 -> max(heap)


#### import heapq
- heapq.heappush() : 원소 추가
- heapq.heappop() : 원소 삭제

```
import heapq

heap = []
heapq.heappush(heap, 3)
heapq.heappush(heap, 5)
heapq.heappush(heap, 2)
heapq.heappush(heap, 7)
print(heap)
# [2, 3, 5, 7]

print(heapq.heappop(heap))
# 2
print(heap)
# [3,5,7]

print(heap[0]) # 삭제하지 않고 읽기
# 3
```


#### 리스트 -> 힙 변환
- heapq.heapify()

```
import heapq

heap = [9,1,3,4,7]
heaq.heapify(heap)
print(heap)
# [1, 3, 4, 7, 9]
```


#### [응용] 최대 힙
```
import heapq

nums = [9,1,3,4,7]
maxheap = []

for num in nums:
    heapq.heappush(maxheap, (-num, num)) # (우선순위, 값)

print(maxheap)
# [(-9, 9), (-7, 7), (-4, 4), (-3, 3), (-1, 1)]

while heap:
    print(heapq.heappop(maxheap)[1], end=' ')
# 9 7 4 3 1
```




## 최단 경로 알고리즘

- 다익스트라 (Dijkstra) : 하나의 정점에서 출발했을 때 다른 모든 정점으로의 최단 경로를 구함
- 플로이드 와샬 (Floyd Warshall) : 모든 정점에서 다른 모든 정점으로의 최단 경로를 구함
![image](https://user-images.githubusercontent.com/79901413/171079039-b314473d-911c-4e40-9889-5c725a52e662.png)
![image](https://user-images.githubusercontent.com/79901413/171079046-d9864fbf-6908-4fbd-ac49-7195f31d80b5.png)


#### 다익스트라 (Dijkstra)

- 다이나믹 프로그래밍을 활용한 최단 경로 탐색 알고리즘
- 특정한 하나의 정점에서 다른 모든 정점으로 가는 최단 경로를 반환
- 음의 간선을 포함할 수 없음 (어차피 현실 세계에는 음의 간선이 존재 X)
- 하나의 최단 거리를 구할 때 그 이전까지 구했던 최단 거리 정보를 그대로 사용


###### 프로그래머스 - 배달 
(https://programmers.co.kr/learn/courses/30/lessons/12978)
이 문제에서
![image](https://user-images.githubusercontent.com/79901413/170931323-bca28f87-f1c9-4c2f-9b86-e1aa650ad21b.png)
1번 부터 6번까지의 노드에 연결된 [거리, 노드] 의 노드 정보가 있을 때

```
dist = [float('inf')] * (N+1) # 1에서 최단거리 저장
dist[1] = 0 # 1은 자기자신 이니까 거리 0

import heapq
def dijkstra(dist, adj):
    heap = []
    heapq.heappush(heap, [0,1]) #거리, 노드
    
    while heap:
        cost, node = heapq.heappop(heap)
        for c, n in adj[node]:
            if cost+c < dist[n]:
                dist[n] = cost + c # 더 짧으면 갱신
                heapq.heappush(heap, [cost+c, n]) # 노드 추가
```
heapq를 사용하여 다익스트라 알고리즘을 구현 가능 (복잡도 O(N*logN))


#### 플로이드 와샬 (Floyd Warshall)

- 모든 정점에서 다른 모든 정점으로의 최단 경로를 반환
- 경유점 개념
    - 두 정점 a, b를 잇는 경로 : 이 경로는 a와 b를 시작점과 끝점으로 가지고, 직접 연결하거나 다른 정점을 경유해서 갈 수도 있음
    - 경로가 거쳐가는 정점들을 '경유점'이라고 함
- 3중 포문으로 시간 복잡도는 O(V^3) -> V가 큰 경우는 피하기


###### 프로그래머스 - 순위
(https://programmers.co.kr/learn/courses/30/lessons/49191)
이 문제는 최단 거리를 구하는 건 아니지만 경유점을 사용하여 연결된 모든 정점을 표시

![image](https://user-images.githubusercontent.com/79901413/171080401-dda3fbc2-0cc2-47d1-a651-8d93ca071a96.png)
[i][j] == 1이라면 i가 j를 이김으로 표현

```
for k in range(1, n+1): # 거쳐가는 노드(기준)
    for i in range(1, n+1): # 출발 노드
        for j in range(1, n+1): # 도착 노드
            if matchs[i][j] == 1 or (matchs[i][k] == 1 and matchs[k][j] == 1):
                matchs[i][j] = 1
```
[i][k] == 1 and [k][j] == 1 일때 [i][j]를 이겼다고 표현할 수 있음 (경유지 k이용)
