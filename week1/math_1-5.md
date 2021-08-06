# CNN 첫걸음

## Convolution 연산 이해하기
- 커널을 입력벡터 상에서 움직여가면서 선형모델과 합성함수가 적용되는 구조
![image](https://user-images.githubusercontent.com/50571795/128470989-15717bcf-a11c-479b-ad1b-adc8442b55bc.png)
- 수식적으로는 다음과 같다.
![image](https://user-images.githubusercontent.com/50571795/128471271-1b6b7424-e1ec-46b1-84f3-611bbb5f41ab.png)
  - 기존 전통적인 Convolution은 빨간색 동그라미 친부분이 - 이나 지금은 +를 사용한다.(+를 사용하는 식은 사실 cross correlation라고 불린다.)
- Convolutions 연산의 수학적인 의미는 신호를 커널을 이용해 국소적으로 증폭 또는 감소시켜서 정보를 추출 또는 필터링 하는 것

### 다양한 차원에서의 Convolution
![image](https://user-images.githubusercontent.com/50571795/128471616-bb782a03-d3e0-473c-9413-4703842a51e8.png)
- 거의 비슷한 모양새를 가진다.

### Convolution 연산의 역전파 이해하기
![image](https://user-images.githubusercontent.com/50571795/128471788-2db5e1ac-8125-4408-bf79-fab36347a28c.png)
- 수식적으로는 위와 같다.
- 역전파를 계산할 때도, convolution 연산이 나오게 된다.


![image](https://user-images.githubusercontent.com/50571795/128471985-fa1b87f7-dfc2-478a-bc4e-45c71e2ac7b1.png)  
forward가 위와 같이 일어나기 때문에 백워드는 아래와 같이 일어난다.  
![image](https://user-images.githubusercontent.com/50571795/128472186-60c7e9de-5037-4160-9014-e410388b0d4c.png)  
웨이트에 대한 갱신은 아래와 같다.
![image](https://user-images.githubusercontent.com/50571795/128472388-493c8c07-f348-4e09-853e-073696a8abfe.png)

# RNN 첫걸음

### 시퀀스 데이터 이해하기
- 소리, 문자열, 주가 등의 연속적인 데이터를 시퀀스 데이터로 분류
- 시퀀스 데이터는 독립동등분포(i.i.d.) 가정을 잘 위배하기 떄문에 순서를 바꾸거나 과거 정보에 손실이 발생하면 데이터의 확률분포도 바뀌게 됩니다.

### 시퀀스 데이터 다루기
- 이전 시퀀스의 정보를 가지고 앞으로 발생할 데이터의 확률분포를 다루기 위해 조건부확률을 이용할 수 있다.
![image](https://user-images.githubusercontent.com/50571795/128472922-8ee4d737-811b-472c-bc1c-f70a775b1c4e.png)
- 위에 식을 조건부 확률을 통해 나타낸 수식이다.
![image](https://user-images.githubusercontent.com/50571795/128473029-294b1cda-4ded-49dc-9cbb-996e90f3e115.png)
- 하지만 이전의 모든 데이터를 다 쓸 수도 없고, 쓸 필요도 없기 때문에 길이 tau를 통하여 조절을 하기도 한다. 하지만 tau가 가변적이어야 되는 경우도 있다.
![image](https://user-images.githubusercontent.com/50571795/128473238-e7900466-4b97-4b73-857c-c269405a5440.png)
- 그러한 경우 아래와 같이 H_t라는 잠재변수를 이용하여 모델을 만든다. 이 방식이 RNN에서 사용되는 방식과 유사하다.
![image](https://user-images.githubusercontent.com/50571795/128473576-b47dd3c4-b03d-4741-8687-324a916d2841.png)

### Recurrent Neural Network 이해하기
- 가장 기본적인 RNN 모형은 MLP와 유사한 모양입니다.
- RNN은 이전 순서의 잠재변수와 현재의 입력을 활용하여 모델링합니다.
- RNN의 역전파는 잠재변수의 연결그래프에 따라 순차적으로 계산합니다.
- BPTT(Backpropagation Through Time)라고 한다.
![image](https://user-images.githubusercontent.com/50571795/128483265-828bb744-c0ca-496d-bd5b-707920efd191.png)
- 수식은 다음과 같다.
![image](https://user-images.githubusercontent.com/50571795/128483703-0a30e8f7-dff3-42d9-8e70-28440f0f643e.png)
- 빨간 부분이 불안정해지기가 쉽다.(=이 부분이 소실되기가 쉽다.)


### 기울기 소실의 해결책
- 시퀀스 길이가 길어지는 경우 BPTT를 통한 역전파 알고리즘의 계산이 불안정해지므로 길이를 끊는 것이 필요합니다.
- 이런 문제들 때문에 Vanilla RNN은 길이가 긴 시퀀스를 처리하는데 문제가 있습니다.
