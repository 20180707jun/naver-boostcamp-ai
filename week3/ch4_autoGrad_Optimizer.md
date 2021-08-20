# 4강 AutoGrad & Optimizer

- 모델은 layer가 여러 개 쌓인 구조로 되어있다.
- 이를 도와주는 것이 ```torch.nn.Module```

### torch.nn.Module
- 딥러닝을 구성하는 layer의 base class
- input. ouput, forward, backward 정의
- 학습의 대상이 되는 parameter(tensor) 정의


### nn.Parameter
- Tensor객체의 상속 객체
- nn.Module 내에 attribute가 될 때는 required_grad=True로 지정되어 학습 대상이 되는 Tensor
- 우리가 직접 지정할 일은 잘 없음
  - 대부분의 layer에는 weights 값들이 지정되어 있음

### Backward
- layer에 있는 parameter들의 미분을 수행
- forward의 결과값과 실제값간의 차이에 대해 미분을 수행
- 해당 값으로 parameter를 업데이트