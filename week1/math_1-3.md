 # 딥러닝 학습방법 이해하기
 ## 신경망을 수식으로 바꾸면
 ![image](https://user-images.githubusercontent.com/50571795/128407279-7f605a1d-88e2-4392-8c97-beca984962a9.png)  

![image](https://user-images.githubusercontent.com/50571795/128407398-ad1e17ba-9d0c-4426-b25a-8ea9aa58ebf4.png)


## softmax 연산
![image](https://user-images.githubusercontent.com/50571795/128408585-35461102-ea8a-4b2c-aa63-8505a70dd77e.png)

- softmax는 모델의 출력을 확률로 해석할 수 있게 변환해주는 연산
- 분류문제를 풀 때, 선형 모델과 소프트 맥스 함수를 결합하여 예측
- 학습을 할 때는 소프트맥스가 필요하지만, 추론시에는 원 핫 벡터를 사용

## 활성함수
![image](https://user-images.githubusercontent.com/50571795/128410064-5308d2dc-7f48-4e94-ade4-8fb0d722e117.png)
- 활성함수를 사용하지 않는다면, 선형모델이 되기 때문에 꼭 사용해야함.
- 전통적으로는 sigmoid와 hyperbolic tangent를 많이 썼으나,
- 최근에는 ReLU를 많이씀

## MLP(다층 퍼셉트론)
### forward propagation
- 아래의 그림은 forward propagation이다.

![image](https://user-images.githubusercontent.com/50571795/128410599-2f76d708-4946-4ec4-9e2e-90fa8fc42920.png)
### 층을 여러개로 쌓는 이유
- 이론적으로는 2층 신경망으로도 임의의 연속함수를 근사할 수 있다.
- 그러나 층이 깊을수록 목적함수를 근사하는데 필요한 뉴런(노드)의 숫자가 훨씬 빨리 줄어들어 좀 더 효율적으로 학습이 가능하다.

### backpropagtion
- forward prop의 역순으로 계산을 하게 됨.

![image](https://user-images.githubusercontent.com/50571795/128411620-8de4aa72-0959-4380-8a54-de471439546c.png)


### 2층 신경망에서의 수식
![image](https://user-images.githubusercontent.com/50571795/128412670-d3d16795-3db4-446f-8bbb-985bbcbf8878.png)


# 확률론 맛보기
## 딥러닝에서 확률론이 필요한 이유
- 딥러닝은 확률론 기반의 기계학습 이론에 바탕을 둠
- loss function들의 작동원리는 데이터 공간을 통계적으로 해석해서 유도
- 회귀 분석에서 손실함수로 사용되는 l2-norm은 예측오차의 분산을 가장 최소화하는 방향으로 학습하도록 유도
- cross-entropy는 모델 예측의 불확실성을 최소화하는 방향으로 학습
- 분산 및 불확실성을 최소화하기 위해서는 측정하는 방법을 알아야 함.

## 이산확률변수 vs 연속확률변수
- 확률변수는 확률분포에 따라 이산형과 연속형으로 구분
- 이산형은 확률번수가 가질 수 있는 경우의 수를 고려하여 확률을 더해서 모델링
![image](https://user-images.githubusercontent.com/50571795/128415643-daa1bfac-ffe2-444e-87df-386c740f7813.png)
- 연속형은 확률변수의 밀도 위에서 적분을 통해 모델링
![image](https://user-images.githubusercontent.com/50571795/128415752-91fc9727-3214-4220-a502-7f3a6de137a2.png)
- 어떤 영역에서는 이산, 어떤 영역에서는 연속인 경우도 있음.

## 몬테카를로 샘플링 방법
- 확률분포를 명시적으로 모를 때,
- 데이터를 이용하여 기대값을 계산하려면 몬테카를로 샘플링 방법을 사용해야함. 
![image](https://user-images.githubusercontent.com/50571795/128418670-0b948678-31ff-49c2-af98-b60a91ca2349.png)
- 몬테카를로 샘플링은 독립추출만 보장된다면 대수의 법칙에 의해 수렴성을 보장한다.
- 위키 : 반복적으로 무작위 추출을 이용하여 함수의 값을 확률적으로 계산하는 알고리즘을 지칭하는 용어

### 몬테 카를로 예제
![image](https://user-images.githubusercontent.com/50571795/128418980-db231bb3-63f9-4edd-a7c4-cedc045f6608.png)

이 방식으로 구했을 때, 1.49387 +- 0.0039 가 나오게 되는데
참값음 1.49364로 거의 비슷하게 나왔음을 알 수 있다.