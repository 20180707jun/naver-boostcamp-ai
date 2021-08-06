# String and advanced function concept

### 문자열 함수
- a.title() : 제목형태로 변환
- a.count('abc') : 문자열a에 'abc'가 들어간 횟수 반환
- a.find('abc') : a에서 왼쪽의 'abc' 인덱스 반환
- a.rfind('abc') : a에서 오른쪽의 'abc' 인덱스 반환
- a.isdigit() : 문자열이 숫자인지 여부 반환
- a.islower() : 문자열이 소문자인지 여부 반환
- a.isupper() : 문자열이 대문자인지 여부 반환

### 특수 문자
문자열 안에서 '\'가 쓰일 때
- \ : 다음줄과 연속임을 표현
- \\\ : \문자
- \" : "문자
- \b : 백 스페이스
- \n : 줄바꾸기
- \t : tab
- \e : esc

## 함수 개발 가이드라인
- 함수는 가능하면 짧게 작성할 것
- 함수 이름에 함수의 역할, 의도가 명확히 들어낼 것
- 하나의 함수에는 유사한 역할을 하는 코드만 포함
- 인자로 받은 값 자체를 바꾸진 말 것

### 함수는 언제 만드는가?
- 공통적으로 사용되는 코든느 함수로 변환
- 복잡한 수식 -> 식별 가능한 이름의 함수로 변환
- 복잡한 조건 -> 식별 가능한 일므의 함수로 변환

### 파이썬 코딩 컨벤션
- 들여쓰기는 tab 또는 4 space
- 일반적으로 4 space
- 한 줄은 최대 79자 까지
- 불필요한 공백 x
- 주석은 항상 갱신
- 코드의 마지막에는 항상 한 줄 추가
- 함수명 소문자, _ 조합
- falke8 모듈로 체크를 할 수 있다.
- 최근에는 __black__ 모듈을 사용한다.

# Python Data Structure

## collections
```py
from collection import deque
from collection import Counter
from collection import OrderedDict
from collection import defaultdict
from collection import namedtuple
```
위의 모듈이 존재함
### deque
- Stack과 Queue를 지원하는 모듈
- rotate, reverse 등 Linked List의 특성을 지원함
- 메모리 구조가 효율적이고, 따라서 처리속도가 빠름
- append, pop을 번갈아서 10^10회 실행했을 때 13.7초, 31.7초로 약 3배 차이

### OrderedDict
- Dict와 달리, 데이터를 입력한 순서대로 dict를 반환함
- 그러나 dict도 python 3.6부터 입력한 순서를 보장하여 출력
```py
# key값으로 정렬
for k, v in OrderedDict(sorted(d.items(), key=lambda t: t[0])).items():
print(k, v)
# value값으로 정렬
for k, v in OrderedDict(sorted(d.items(), key=lambda t: t[1])).items():
print(k, v)
```
### defaultdict
- Dict type의 값에 기본 값을 지정 신규 값을 생성시에 사용하는 방법
```py
d = dict()
print(d['first']) # KeyError 발생 : key 값이 지정되지 않은상태이기 떄문

from collections import defaultdict
d = defaultdict(object)
d = defaultdict(lambda : 0)
print(d['first']) # 0이 출력 : defaultdict은 value를 할당하지 않은 key값들에 대해서 0을 default로 설정
```
### Counter
- Sequence type의 data element들의 갯수를 dict형태로 반환

```py
from collections import Counter

c = Counter()
c = Counter('gallahad')
print(c) # Counter({'a': 3, 'l': 2, 'g' 1, 'd': 1, 'h': 1})
```
- Counter를 기반으로 list를 만들 경우
```py
c = Counter({'red' :4, 'blue' : 2})
print(c)
print(list(c.elements()))
# Counter({'red': 4, 'blue'' : 2})
# ['blue', 'blue', 'red', 'red', 'red', 'red']
```
- set의 연산자를 지원함
```py
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=2, d=4)
c.subtract(d)
print(c) # Counter({'a' : 3, 'b': 0, 'c': -3, 'd': -6})
```
```py
c = Counter(a=4, b=2, c=0, d=-2)
d = Counter(a=1, b=2, c=3, d=4)
print(c + d)
print(c & d)
print(c | d)
# Counter({'a': 5, 'b': 4, 'c':3, 'd': 2})
# Counter({'b': 2, 'a': 1})
# Counter({'a': 4, 'd': 4, 'c' : 3, 'b' : 2})
```

### namedtuple
- tuple형태로 data 구조체를 저장하는 방법
- 저장하는 data의 variable을 사전에 지정해서 저장함
```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)
print(p[0] + p[1])
x, y = p
print(x, y)
print(p.x + p.y)
print(Point(x=11, y=22))
# 33
# 11 22
# 33
# Point(x=11, y=22)
```


# Pythonic code
- 파이썬 스타일의 코딩 기법
- 파이썬 특유으의 문법을 활용하여 효율적으로 코드를 표현함
- 그러나 더이상 파이썬 특유는 아님, 많은 언어들이 서로의 장점을 채용
- 고급 코드를 작성 할 수록 더 많이 필요해짐

### 주로 쓰이는 것들
- split & join
- list comprehension
- enumerate & zip
- lambda & map & reduce
- generator
- asterisk


#### list comprehension
```py
# if문 1
result = [i+j for i in case_1 for j in case_2 if not(i==j)]
# if문 2
result1 = [i+j if not(i==j) else i for i in case_1 for j in case_2]

# if 문만 쓸 때는 맨 뒤로,
# else까지 쓸 때는 중간으로 

# for i in case_1 for j in case_2
# ==
# for i in case_1:
#     for j in case_2:
```
__tip__
- pprint를 이용하면 print를 이쁘게 볼 수 있다.
```py
import pprint
pprint.pprint(~~~)
```

#### reduce
``` py
from functools import reduce
print(reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
# 15
```
![image](https://user-images.githubusercontent.com/50571795/128278381-97d59796-86a5-477c-adb8-62de6fe827bf.png)

- 그러나 코드의 직관성이 떨어져서 lambda나 reduce는 python3에서 사용을 권장하지 않음
- legacy libary이지만 다양한 머신러닝 코드에서 여전히 사용중

### generator

#### generator comprehension
```py
gen_ex = (n*n for n in range(500))
print(type(gen_ex)) # <class 'generator'>
```

### variable-length asterisk
- 개수가 정해지지 않은 변수를 함수의 parameter로 사용한느 법
- Asterisk(*)를 사용하여 함수의 parameter를 표시함
- 입력된 값은 tuple type으로 사용할 수 있음
- 가변인자는 마지막에 한개만 넣어줄 수 있음ㅍ  
```py
# ex
def asterisk_test(a, b, *args):
    return a+b+sum(args)
print(asterisk_test(1, 2, 3, 4, 5))
```

### Keyword variable-length
- parameter 이름을 따로 지정하지 않고 입력하는 방법
- **를 사용하여 함수의 parameter를 표시함
- 입력된 값은 dict type으로 사용할 수 있음

```py
# ex
def kwargs_test_1(**kwargs):
    print(kwargs)
kwargs_test_1(first=3, second=4, third=5)
```