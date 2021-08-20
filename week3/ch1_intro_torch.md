# Introduction to PyTorch

## TensorFlow vs PyTorch  
![image](https://user-images.githubusercontent.com/50571795/129649257-7ae0f9b8-0a0d-4659-a5be-32de89300f37.png)
- 가장 큰 차이는 그래프를 그리는 것(마지막 빨간 네모)

Define and Run(TensorFlow)
- 그래프를 먼저 정의 -> 실행시점에 데이터 feed

Define by Run(Dynamic Computational Graph, DCG)(torch)
- 실행을 하면서 그래프를 생성하는 방식

### torch의 사용 이유
- define by Run의 장점
  - 즉시 확인 가능 -> pythonic code
- GPU supprot, Good API and community
- 사용하기 편함이 가장 크다.
- TF는 production과 scalability의 장점이 있다.

**Numpy + AutoGrad + Function**
- Numpy구조를 가지는 Tensor객체로 array를 표현
- 자동 미분 지원
