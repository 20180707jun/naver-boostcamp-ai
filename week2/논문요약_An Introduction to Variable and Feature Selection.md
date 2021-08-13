# An Introduction to Variable and Feature Selection
대략의 흐름은 이렇다.
- fs란 무엇인가? : 3가지 방법론이 있다.
  - filters
    - variable ranking
  - wrappers
  - embedded
---
논문에서는 variable과 feature라는 용어가 계속 나온다.
- variable : the "raw" inpu variables
- feature : variables constructed for the input variables  

라고 되어있다.

---
fs와 비슷한 개념들
- Feature Engineering : 도메인 지식을 사용하여 데이터에서 피처를 변형/생성
- Feature Extraction : 차원축소 등 새로운 중요 피처를 추출
- Feature Selection : 기존 피처에서 변겅없이 원하는 피처만 선택    

논문에서는 Feature Selection를 메인, Feature Extraction이 짧게 에 대해서 서술되어 있음.

## Abstract
- fs의 목적은 3가지이다.
  - predictor의 성능을 높이기 위함
  - 좀 더 빠르고, 효율적인 predictor를 만들기 위함
  - 데이터를 생성한 underlying process를 더 잘 이해하기 위함

## Introduction
- fs는 많은 이점들이있다.
  - 데이터에 대한 시각화나 이해를 용이하게 한다.
  - 비용(연산량, 시간)을 줄인다.
- 여기 논문에서는 predictor를 유용하게 만드는 포인트에 집중한다.


check list
1. 도메인 지식이 있는가? : 그렇다면, 적절한 feature를 만들어서 사용
2. 데이터가 commensurate한가? : 아니라면, normalize
3. 데이터가 interdependence한가? : 그렇다면, feature set늘려서 conjunctive하게 만들어라.
4. input variables를 prune할 필요가 있는가? : 아니라면, 

## 2. Variable Ranking
- variable ranking으로 된 fs 알고리즘이 많다. 간단하고, 성능이 괜찮고, scalability하기 때문.
- predictor를 만드는 데에 필수적이지는 않다.


### 2.1 principle of the method and notations
- Kohavi and John의 classification에 따르면 variable ranking은 filter method이다. 
  - 이 말은 전처리과정이라는 뜻이다.
  - 또한 특정 가정이 주어질 때, 최적의 결과를 predictor에게 줄 수 있다.

## 2.2 Correlation Criteria
- target과  varable의 linear dependency를 확인 할 수 있다.

## 2.3 Single Variable Classifiers
- 하나 더 확장해볼 수 있는 점은 그들의 예측 파워에 따라

## Conclusion
- 선형 predictor를 사용하는 것을 추천한다.
- fs는 2가지 방법을 추천한다. 
  - variable ranking metod를 이용해라(상관계수, 또는 다른 기타 정보들로)
  - nested subset selection method를 사용해라.(forward or backward selection을 이용하여 또는 multiplicative updates를 이용하여)
- 더나아가 관찰데이터를 실험데이터로 만들기 위해, 또 causality inference 문제를 해결하기 위해서, fs와 실험 설계를 연결할 필요가 있다.

## 요약하자면...
An Introduction to Variable and Feature Selection

이 논문은 feature selection을 소개한다.
- fs의 목적은 3가지이다.
  - predictor의 성능을 높이기 위함
  - 좀 더 빠르고, 효율적인 predictor를 만들기 위함
  - 데이터를 생성한 underlying process를 더 잘 이해하기 위함
- 이중에서 predictor의 성능을 높이기 위한 방법을 주로 설명한다.
- 방법에는 3가지가 있다.
  - filter : predictor에 상관없이 변수만을 보고 고른다.
    - ex) 
    - correlation coefficient를 이용하여 변수를 고름.
  - wrapper : 우리가 이용하는 learning machine을 black box로 보고, predictive power를 이용해서 subset of variable의 score를 매긴다.
    - ex) 
    - forward selection : feature를 하나씩 넣어가며 모델의 성능을 측정하고, 가장 좋은 feature subset을 선택한다.
    - backward selection : 반대로 모든 feature를 넣어두고 하나씩 빼면서 성능에 가장 영향도가 적은 feature를 찾는다.
    - genetic algorithms, ...
  - embedded : 학습 단계에 fs를 넣는다.
    - ex)
    - lasso : l1-norm을 통해 제약을 건다.
    - ridghe : l2-norm을 통해 제약을 건다.
    - Elastic Net : 위 둘을 선형 결합한 방법.
    - 위의 방식들은 검색 참고 [링크](https://subinium.github.io/feature-selection/)


---
3줄 요약 방법
- 어떤 문제를 풀기위함 ?
- 기존 방법 ?
- 이 논문에서는 ?
