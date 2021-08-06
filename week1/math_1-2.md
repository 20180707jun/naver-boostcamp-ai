# 경사하강법 순한맛


### 미분이 뭔가요?
- 밑의 코드로 미분을 코딩할 수 있다.
```py
import sysmpy as sym
from sympy.abc import x

sym.diff(sym.poly(x**2 + 2*x + 3), x)

poly(2*x +2, x, domain='ZZ')
```

### 경사하강법 알고리즘
- 경사하강법에 대한 알고리즘을 python으로 작성한 것
```py
# gradient : 미분을 계산하는 함수
var = init
grad = gradient(var)
while (abs(grad)>eps):
    var = var - lr * grad
    grad = gradient(var)
```
``` py
# gradient : 그레디언트 벡터를 계산하는 함수

var = init
grad = gradient(var)
while (norm(grad) > eps): # 절댓값 계산이 안되기 때문에 norm사용
    var = var - lr * grad
    grad = gradient(var)
```

#### 변수가 벡터이면?
- 벡터가 입력인 다변수 함수의 경우 편미분을 사용한다.
- 각변수별로 편미분을 계산한 그레디언트 벡터를 이용하여 경사하강/경사상승법에 사용할 수 있다. 
- 그레디언트 벡터에 음수를 취해서 업데이트를 하는데 이용한다.
![image](https://user-images.githubusercontent.com/50571795/128117086-de9c5840-9de2-47b0-916a-89b3bbffef81.png)

예시는 다음과 같다.
![image](https://user-images.githubusercontent.com/50571795/128116594-39bc4137-6465-4a4f-898e-d3482bcf4a54.png)


# 경사하강법 매운맛

### 경사하강법 기반 선형회귀 알고리즘

```py
for t in range(T):
    error = y- x @ beta
    grad = - transpose(X) @ error
    beta = beta - lr * grad
```
종료조건을 일정 학습 횟수로 바꾸었다.

### 경사하강법은 만능일까?
- 적절한 학습률과 학습횟수를 선택했을 때 수렴을 할 수 있다.
- 비선형 회귀의 문제는 로컬 미니멈에 빠질 수 있다.

### 확률적 경사하강법(SGD : stochastic gradient descent)
- 딥러닝의 경우 sgd가 gd보다 실증적으로 더 낫다고 검증되었다.

#### 확률적 경사하강법의 원리 : 미니배치 연산
- 미니 배치를 가지고 그레디언트 벡터를 계산함.
- 미니배치는 확률적으로 선택하므로 목적식 모양이 바뀌게 됨.
- 매번 다른 미니 배치를 사용하기 때문에 곡선 모양이 계속 바뀌게 됨.
- 미니배치로 경사하강법을 하기때문에 계산량이 적음.


# 메모
git checkout -b test2
git push origin test2
-> compare pull request 보내기
pr log 확인

- 소프트웨어 기업
  - 기본적인 것, 원론적인 것에 집중하라.
  - 모든 것을 커버할 수 있는 사람을 필요.
  - 따라서 최신 경향보다 기본이 더 중요.
- 대기업
  - 뭔지 잘 모름
  - 기술이 필요하면 사는 경향
  - 뭐해봤음? 뭐해보고싶음?

- 취업
  - cv 미리 작성하기
  - 링크드인 
- 할 것
  - 일주일 세 문제
  - 논문 일주일 1개