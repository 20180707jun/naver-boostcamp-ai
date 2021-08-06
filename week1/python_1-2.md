# Variables
- 2-1 ~ 2-3


#### 폰 노이만 아키텍처

![image](https://user-images.githubusercontent.com/50571795/128061851-60729b7d-6811-46e2-9b93-ff6f34ff84b5.png)

- cpu = 제어장치 + 산술장치

#### 변수명 
- 변수명은 줄이지 않는 것을 권장한다.

#### Dynamic Typing
- 코드 실행시점에 데이터의 Type을 결정하는 방법

#### 슬라이싱
- 슬라이싱은 범위가 넘어가면 최댓값으로 지정됨

#### parameter
- 함수의 입력 값

#### argument
- 실제 parameter에 대입된 값


### formatting
1. % string
2. format 함수
3. fstring
```py
print("%d %d %d" % (1, 2, 3))
print("{} {} {}".format("a", "b", "c"))
print(f"value is {value}")
```  
old-school formatting
- 일반적으로는 %-format 과 str.format() 함수를 사용함
```py
print('%s %s' %('one', 'two'))
print('{} {}'.format('one', 'two'))
print('%d %d' % (1, 2))
print('{} {}'.format(1, 2))
```
- %-format
```py
print("Art: %5d, Price per Unit : %8.2f" % (453, 59.058))
```
- str.format()
  - 앞의 숫자 0, 1은 format의 인자의 순서와 일치함.
```py
print("Art: {0:5d}, Price per Unit: {1:8.2f}".format(453, 59.058))
```
#### padding
```py
print("Product: %5s, Price per unit: %.5f." % ("Apple", 5.243))
print("Product: {0:5s}, Price per unit: {1:.5f}.".format("Apple", 5.243))
print("Product: %10s, Price per unit: %10.3f." % ("Apple", 5.243))
print("Product: {0:>10s}, Price per unit: {1:10.3f}.".format("Apple", 5.243))
```

#### f-stirng
```py
name = "Sungchul"
age = 39
print(f"Hello, {name}. You are {age}.")
print(f'{name:20}')
print(f'{name:>20}')
print(f'{name:*<20}')
print(f'{name:*>20}')
print(f'{name:*^20}')
```
```
Hello, Sungchul. You are 39.
Sungchul
Sungchul
Sungchul************
************Sungchul
******Sungchul******
3.14
```

## Conditionals and Loops

![image](https://user-images.githubusercontent.com/50571795/128070251-f1b09a76-89b3-4cde-a9bd-0420658d9708.png)

#### 삼항 연산자
```py
is_even = True if value % 2 ==0 else False
```
### debugging
- 코드의 오류를 발견하여 수정하는 과정
- 오류의 원인을 알고 해결책을 찾아야 함
- 문법적 에러를 찾기 위한 에러 메시지 분석
- 논리적 에러를 찾기 위한 테스트도 중요