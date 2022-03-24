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
