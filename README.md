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
