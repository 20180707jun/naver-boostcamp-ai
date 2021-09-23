# python scope

scope는 다음과 같다.
![image](https://user-images.githubusercontent.com/50571795/133557583-cca26f03-a10b-427d-9995-89ad01e30c2b.png)
- Builtin Scope
- Module Scope(Global)
- Enclosing Scopes(Nonlocal)
- Local Scope

## Local Scope
```py
def func():
    a=1
    print(a) # print 1

print(a) # error
```
- local scope는 위와 같이 함수나 객체 안에서 호출되는 변수의 번위를 의미한다.

## Enclosing Scope
```py
def outer():
    a=1
    print(a)

    def inner():
        b = 7
        print(a*b) # 여기서는 a, b 모두 접근 할 수 있다. 7 출력
    inner()
    print(b) # error
```
- 부모 함수에서 선언되는 변수는 중첩함수 안에서도 유효한 범위를 갖는다.

## Global Scope
```py
k = 9

def outer():
     a= 1
     print(a + k)

     def inner():
        b = 7
        print(a* b* k)
    inner()
outer()
print(k)

'''
1
63
9
'''
```

- 위의 print는 전부 출력이 된다.

## Built-in Scope
- 파이썬 안에 내장되어 있는, 파이썬이 제고앟는 built-in 속성, 함수들의 scope이다.
- e.g., len, del 등이 이에 속한다.

## Shadowing
- 파이썬은 변수나 함수를 찾을 때 다음의 순서로 찾게 된다.
- ```Local -> Enclosing -> Global -> Built-in```
- 안에 있는 것이 밖의 것을 가리게 되는데 이를 shadowing이라고 한다.



## 내가 궁금했던 것
[링크](https://soooprmx.com/python-namespace-and-variable-scope/) 참고
```py
x = 10
 
def func():
    x = x + 1 # UnboundLocalError : local variable 'a' referenced before assignment
    print(x)
 
func()
```
위와 같은 예시도 있다.  
위에서 설명한 shadowing을 적용한다면 x를 global에서 찾아서 연살을 해야되지 않을까 생각이 든다.  
하지만 오류가 난다. 이유는 ```x = ```시점에서 로컬 변수를 초기화하고 네임 스페이스에 등록해버린다. 그러니까 여기서의 x는 글로벌 변수가 아니라 로컬 변수인 것이다.  

```py
x = 10
def func():
    print(x)
    x = x + 1 # UnboundLocalError : local variable 'a' referenced before assignment
    print(x)
 
func()
```

오해하는 부분은 다음과 같다.
- 파이썬은 인터프리터 언어니까 한 줄씩 해석하고 처리한다.
- 따라서 ```print(x)```시점에서 x는 로컬에 정의되지 않았으므로 전역변수이다. 10을 출력한다.
- 두번째 ```print(x)```시점에서 4를 출력한다.

하지만 현실은 다음과 같다.
- 파이썬이 "한 번에 한줄씩"처리하는 것은 모듈을 로드할 때 뿐이다. 따라서 파이썬 해석기가 소스코드를 받아서 실행하기 전에 모든 해석이 이루어진다.
- 해석이 이루어진 후에 소스코드는 컴파일된 바이트코드로 번역된 상태로 메모리에 탐재도니다.
- 따라서 ```print(x)```문이 실행되기 이전에 x의 위치는 로컬 네임 스페이스로 정해진다. 그런데 아직 x가 정의 되지 않았다.
- 따라서 첫 번째 ```print(x)```에서 ```NonLocalBoundError``` 가 발생한다.

shadowing은 읽는 시점에서만 적용이 된다. 그리고 함수 내에서 대입식의 좌변으로 표시되는 모든 변수는 로컬 변수로 간주된다. 

따라서 global 또는 nonlocal이라는 키워드를 통해서 상위 스코프의 변수를 사용한다고 먼저 명시해야한다.



```py
def outer():
    a = 1
    print(a)
    
    def inner():
        b=7
        print(a*b) # UnboundLocalError : local variable 'a' referenced before assignment
        a=3
        print(a*b)
    inner()
    print(a)
    print(b)
```
위의 함수들은 실행이 될까? 정답은 아니다. 