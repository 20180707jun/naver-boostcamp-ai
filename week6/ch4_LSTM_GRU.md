# 4강 LSTM and GRU

## LSTM(Logh Short-Term Memory)
- gradient vanishing or exploding에 더 나은 성능을 보인다.

![image](https://user-images.githubusercontent.com/50571795/133717726-30e161ff-268c-461b-a549-db37030e9230.png)  
구조는 위와 같다.  
조금더 세부적으로 본다면 4개의 게이트가 있다.
- i : Input gate, Whether to write to cell
- f : Forget gate, Whether ot erase cell
- o : Output gate, How much to reveal cell
- g : Gate gate, How moch to write to cell

![image](https://user-images.githubusercontent.com/50571795/133717957-6a0ac5e8-41a5-4022-8b81-557ffbef5c33.png)  

### forget gate
![image](https://user-images.githubusercontent.com/50571795/133718000-b41fb7bd-44a1-46da-a605-86758075fddc.png)

![image](https://user-images.githubusercontent.com/50571795/133724743-d812b339-028f-4d97-935f-d7f34cf27041.png)
- LSTM에서 long-term dependency 문제를 해결하기 위해서 생각한 것이 바로 저기 있는 cell state이다.
- cell state는 과거부터의 정보를 계속 가지고 있는 역할을 하는데, 이 정보를 forget gate에서 얼만큼 잊을지를 정한다.
- ![image](https://user-images.githubusercontent.com/50571795/133726264-b405fb84-f657-4e8f-a2c1-0a27e8e59751.png)
- 위와 같은 방식이다. sigmoid를 통과한 벡터를 곱해주어 값을 기존보다 줄인다.

### input gate
![image](https://user-images.githubusercontent.com/50571795/133726695-56038311-8907-44f7-a7ba-b186b9ee4677.png)
- ![image](https://user-images.githubusercontent.com/50571795/133726787-13c617e6-32f0-44db-91a9-ffb082f6cdb6.png)
- ![image](https://user-images.githubusercontent.com/50571795/133726735-54eeb809-5641-438f-9905-f5ac9922d4d0.png)
- 수식은 위와 같다. 더 해줘야할 C_tilde를 만들어내고, 그 것을 얼만큼 곱해야할지에 대해 sigmoid를 통과한 i_t를 곱해준다.
- tanh연산을 하는 부분은 gate gate라고 한다.

### output gate
![image](https://user-images.githubusercontent.com/50571795/133727111-4d4f27b5-f88e-4b15-8a91-2ab721f77760.png)
- ![image](https://user-images.githubusercontent.com/50571795/133727137-1c746313-cc5a-4256-abcd-e2283df48a84.png)

## GRU Gated recurrent Unit(GRU)
![image](https://user-images.githubusercontent.com/50571795/133727225-2d7aab10-5c68-42c4-87e0-841a29801bd5.png)
- ![image](https://user-images.githubusercontent.com/50571795/133727205-fd8bbcd3-edbf-470c-b915-dae6d5d8a336.png)
- 수식은 위와같다.
- 연산을 줄여서 메모리와 속도적인 측면을 개선하였다.
- cell state vector와 hidden state vector를 합쳤다.
- GRU의 h는 lstm의 c에 가까운 의미를 가진다.(과거부터의 정보를 갖고있다.)
- 수식의 맨 마지막 h_t에 대한 설명과 c.f) 부분이 차이점이다.
- GRU는 h_tilde와 h_t-1에 대해서 가중평균을 취했다.


### Backpropagation in LSTM GRU
![image](https://user-images.githubusercontent.com/50571795/133727573-51a75943-1211-4d4f-90ce-ebd030ecd018.png)
- 그림에서 보면 새로운 정보를 넣어줄 때 덧셈연산으로 더해주게 되는데, 이 부분이 vanishing gradient문제를 해결하는데 큰 영향을 주었다.
- 덧셈연산은 backprob 시에 이전 gradient를 유지하는 역할을 하기 떄문이다.


## Summary RNN/LSTM/GRU
- RNN은 굉장히 유연한 구조이다.
- Vanilla RNN은 간단하지만 제대로 동작하지 않는다.(vanishing gradient, exploding, long-term dependency 약함)
- 일반적으로 LSTM과 GRU를 사용하는데 이는 gradient flow를 향상시켰다.