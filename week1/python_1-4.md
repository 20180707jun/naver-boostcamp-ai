# Python Object Oriented Programming
## OOP의 3요소
- Inheritance
- Polymorphism
- Visipility

### Inheritance(상속)
- 부모클래스로 부터 속성과 Method를 물려받은 자식 클래스를 생성하는 것
### Polymorphism(다형성)
- 같은 이름 메소드의 내부 로직을 다르게 작성
- Dynamic Typing 특성으로 인해 파이썬에서는 같은 부모클레스의 상속에서 주로 발생함.
- 중요한 OOP의 개념 그러나 너무 깊이 알 필요X
### Visibility(가시성)
- 객체의 정보를 볼 수 있는 레벨을 조절하는 것
- 누구나 객체안에 모든 변수를 볼 필요가 없음


## decorator
알아둘 3가지 개념
- first-class object
- inner function
- decorator

### First-class objects
- 일등함수 또는 일급 객체
- 변수나 데이터 구조에 할당이 가능한 객체
- 파라메터로 전달이 가능 + 리턴 값으로 사용
```py
ex
# 함수를 변수로 사용
def square(x):
    return x * x
f = squre
f(5)
# 함수를 파라메터로 사용
def square(x):
    return x * x
def cube(x):
    return x*x*x
def formula(method, argument_list):
    return [method(value) for value in argument_list]
# 함수 내에 또 다른 함수가 존재
def print_msg(msg):
    def printer():
        print(msg)
    printer()
print_msg("Hello, Python") 
# closure example
def tag_func(tag, text):
    text = text
    tag = tag
    def inner_func():
        return '<{0}>{1}<{0}>'.format(tag, text)

    return inner_func
h1_func = tag_func('title', 'This is Python Class')
p_func = tag_func('p', 'Data Academy')
```

# Module and Project
## Module
- 프로그램에서는 작은 프로그램 조각들, 모듈들을 모아서 하나의 큰 프로그램을 개발함
- 프로그램을 모듈화 시키면 다른 프로그램이 사용하기 쉬움
  - ex) 카카오톡 게임을 위한 카카오톡 접속 모듈
- 쉽게 생각하면 import 해오는 것들이 모듈이라고 할수 있음.
### Module 만들기
- 파이썬의 Module == py 파일을 의미
- 같은 폴더에 Module에 해당하는 .py 파일과 사용하는 .py을 저장한 후
- import 문을 사용해서 module을 호출
### namespace
- 모듈을 호출할 때 범위 정하는 방법
- 모듈 안에는 함수와 클래스 등이 존재 가능
- 필요한 내용만 골라서 호출 할 수 있음
- from 과 import 키워드를 사용함

## Package
- 하나의대형프로젝트를만드는코드의묶음
- 다양한모듈들의합, 폴더로연결됨
- \_\_init\_\_ , \_\_main\_\_ 등키워드파일명이사용됨
- 다양한오픈소스들이모두패키지로관리됨

## Python 가상환경
- 프로젝트 진행시 필요한 패키지만 설치하는 환경
  - virtualenv + pip
  - conda
  - 두 가지가 있음


# Exception/File/Log Handling
## Exception
### 예상 가능한 예외
- 발생 여부를 사전에 인지할 수 있는 예외
- 사용자의 잘못된 입력, 파일 호출 시 파일 없음
- 개발자가 반드시 **명시적으로 정의**해야함
### 예상 불가능한 예외
- **인터프리터 과정에서 발생하는 예외**, 개발자 실수
- 리스트의 범위를 넘어가는 값 호출, 정수 0으로 나눔
- 수행 불가시 인터프리터가 자동 호출

예외가 발생할 경우 후속 조치등 대처가 필요
### Exception Handling
```py
# ~try ~except ~else
try:
    예외 발생 가능 콛
except <Exception Type>:
    예외 발생시 동작하는 코드
else:
    예외가 발생하지 않을 때 동작하는 코드
```
```py
# ~try ~except ~finally
try:
    예외 발생 가능 코드
except <Exception Type>:
    예외 발생시 동작하는 코드
finally:
    예외 발생 여부와 상관없이 실행됨
```
#### raise 구문
- 필요에 따라 강제로 Exception을 발생
```py
## ex
while True:
value = input("변환할 정수 값을 입력해주세요")
for digit in value:
    if digit not in "0123456789":
        raise ValueError("숫자값을 입력하지 않으셨습니다")
print("정수값으로 변환된 숫자 -", int(value))
```
#### assert
- 특정 조건에 만족하지 않을 경우 예외 발생
```py
# ex
def get_binary_nmubmer(decimal_number):
    assert isinstance(decimal_number, int)
    return bin(decimal_number)

print(get_binary_nmubmer(10))
```

## File Handling
- os에서 파일을 저장하는 **트리구조** 저장 체계

## Logging Handling

### logging

- 프로그램이 실행되는 동안 일어나는 정보를 기록을 남기기
- 유저의 접근, 프로그램의 Exception, 특정 함수의 사용
- Console 화면에 출력, 파일에 남기기, DB에 남기기 등등
- 기록된 로그를 분석하여 의미있는 결과를 도출 할 수 있음
- 실행시점에서 남겨야 하는 기록, 개발시점에서 남겨야하는 기록

### logging module

Python의 기본 log 관리 모듈
```py
import logging

logging.debug("틀렸잖아!") 
logging.info("확인해")
logging.warning("조심해!") # 기본 logging level이 waring이상 
logging.error("에러났어!!!") # 부터이기 때문에 console에는 여기서부터 출력
logging.critical ("망했다...")
# 조심해!
# 에러났어!!!
# 망했다...
```
```py
logger = logging.getLogger("main")
logging.basicConfig(level=logging.Debug) # 여기서 최소 console출력을 바꿀 수 있다.
```
```py
# 보통은 stream_handler를 사용하여 log 관리
stream_handler = logging.FileHandler("my.log", mode='w', encoding='utf8')
logger.addHandler(stream_handler)
```


- 프로그램 진행 상황에 따라 다른 Level의 Log를 출력함
- 개발 시점, 운영 시점 마다 다른 Log가 남을 수 있도록 지원함
- DEBUG > INFO > WARNING > ERROR > Critical
- Log 관리시 가장 기본이 되는 설정 정보

**log level별 의미**
![image](https://user-images.githubusercontent.com/50571795/128447695-a75f8f7f-9dea-472a-a71d-fc7802305f91.png)

### config

### configparser
- 프로그램의 실행 설정을 file에 저장함
- Section, Key, Value 값의 형태로 설정된 설정 파일을 사용
- 설정파일을 Dict Type으로 호출후 사용

```
[SectionOne]
Status: Single
Name: Derek
Value: Yes
Age: 30
Single: True

[SectionTwo]
FavoriteColor = Green

[SectionThree]
FamilyName: Johnson
```

```py
import configparser
config = configparser.ConfigParser()
config.sections()
config.read('example.cfg')
config.sections()
for key in config['SectionOne']:
    print(key)
config['SectionOne']["status"]
```
위의 파일을 읽어올 수 있음.

#### argparser
```py
# ex
import argparse
parser = argparse.ArgumentParser(description='Sum two integers.')
parser.add_argument('-a', "--a_value", dest=”A_value", help="A integers", type=int)
parser.add_argument('-b', "--b_value", dest=”B_value", help="B integers", type=int)
args = parser.parse_args()
print(args)
print(args.a)
print(args.b)
print(args.a + args.b)
```

### logging formmater
``` py
# ex
formatter = logging.Formatter('%(asctime)s %(levelname)s %(process)d %(message)s')
```