# 9강 Hyperparameter Tuning
성능이 안나올 때,
1. 모델 바꾸기 
2. 데이터 추가, 바꾸기, 확인
3. hyperparam tuning

2번이 가장 중요하다. 모델은 이미 비슷하게 알고 있기에 차이가 크지 않음. 3번은 마른 수건 짜내기

## Hyperparameter Tuning
- 모델 스스로 학습하지 않는 값은 사람이 지정(learning rate, 모델의 크기, optimizer 등)
- 하이퍼 파라미터에 의해서 값이 크게 좌우 될 때도 있음
- 마지막 0.01을 쥐어짜야 할 때 도전해볼만 하다.

### grid vs random
- 가장 기본적인 방법 grid vs random
- 최근에는 베이지안 기반 기법들이 주도(BOHB bayesian optimization hyper band)
![image](https://user-images.githubusercontent.com/50571795/130347725-f732aabc-cbe4-4ac4-b180-fd762622950e.png)

#### 도구 : Ray
- multi-node multi processing 지원 모듈
- ML/DL의 병렬 처리를 위해 개발된 모듈
- 기본적으로 현재의 분산병렬 ML/DL 모듈의 표준
- Hyperparameter Search를 위한 다양한 모듈 제공

Hyperparameter tunning은 성능이 많이 오르지 않는 경우가 많다.
data를 최우선, 그 다음은 모델, 그 다음은 tunning