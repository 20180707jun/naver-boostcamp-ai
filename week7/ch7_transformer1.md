# 7강 transformer 1

transformer에 대한 내용이다.

구조는 아래와 같다.

![image](https://user-images.githubusercontent.com/50571795/134287671-45d813e2-0a2e-4284-a64a-6c578af6e997.png)

기존에 사용되었던 CNN, RNN의 구조가 없어진 것을 볼 수가 있다. attention 모듈만을 사용해서 만든 모델이 바로 transformer이다.

## 연산 개략도
![image](https://user-images.githubusercontent.com/50571795/134288194-d963808c-4b71-4966-ab00-e1f19453c4a6.png)

개략적인 연산 과정은 위와 같다.

query, key, value 벡터를 만들어내는 과정이다. Q와 K의 내적을 통해서 value가 얼만큼 들어가야 할지 softmax를 통해서 나타낸다. 그 후 구해진 softmax값에 value를 곱하여, 저러한 그림을 나타낸다.

*여기서 왠지 Q와 K를 합쳐 놓은 벡터로 만들어서 연산량을 좀 줄일 수 있지 않을까? 하는 생각이 든다. 아마도 내가 식견이 얕기 때문에 하는 생각인 것 같다. 아직 Q, K의 정확한 이해가 모자라다.*

수식적으로는 다음과 같다. 간단한 수식이다.

![image](https://user-images.githubusercontent.com/50571795/134288460-9d3dffb4-014e-4230-b23a-872019722623.png)

실제 연산에서는 root d_k를 나눠주게 되는데, 이는 Q*K_T를 하게 되면 분산이 D배 늘어나게 되고, 이를 보정하고자 표준편차인 root D를 나눠주는 것이다.

위와 같이 분산을 보정해주지 않는다면, softmax시에 값이 너무 커져서 큰 값을 제외하고는 극도로 작은 값을 갖게되는 것을 알 수 있다.

![image](https://user-images.githubusercontent.com/50571795/134288539-7b38c3ec-2137-486a-813a-71df932aff1e.png)


