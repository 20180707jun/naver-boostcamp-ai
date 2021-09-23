# 5강 Seq2Seq

![image](https://user-images.githubusercontent.com/50571795/133727971-d4dfc532-9c61-4c19-8520-6d37297b7994.png)
- many to many에 해당한다.
- 구조는 아래와 같다.

![image](https://user-images.githubusercontent.com/50571795/133729826-f0661378-2dca-4d5c-b573-d053518c2508.png)  
위과같은 구조는 마지막 thought vector에 모든 seq정보가 함축되어있다. 이렇게되면 순서상 앞쪽에 있는 단어들의 정보가 유실될 수가 있다. 아무리 LSTM, GRU가 이러한 문제를 해결했어도 말이다.  

그렇기 때문에 여기서는 Attention module을 도입한다.  
![image](https://user-images.githubusercontent.com/50571795/133731859-c053cd31-24b0-4ef9-8c38-e4cf2e056f19.png)  
잘 보면 한 블록마다 h1, h2 라는 hidden embedding에 대해서 필기를 해주신 부분이 있다. 이 부분을 바로 Attention module의 아이디어라고 볼 수 있을 것 같다.

![image](https://user-images.githubusercontent.com/50571795/133964227-c7760095-291b-4845-8d9b-909e6176c5a2.png)  
위의 그림은 seq2seq의 구조이다. decoding vector에 각 encoding vector를 곱하여 나온 것이 Attention score이다. 여기서 attentions score에 softmax를 취하면서 attention distribution이 만들어지게 된다.  
나온 softmax 값들에 각 벡터들을 가중평균을 구하면 그 vector가 attention output이 된다. 그 후에 decoding vector와 attention vector가 concat되어 나오게 된다.  
이 과정을 end token이 나올 때 까지 반복 한다.

#### teacher forcing
![image](https://user-images.githubusercontent.com/50571795/133966274-a406053b-6927-4653-a46a-d24ffc5aa738.png)  
training을 시킬 때, 나오는 output을 다음 input으로 넣어주다보면, 문제가 생길 수 있다. output이 제대로 나오지 않았을 때, input으로 넣어주게 되면 다음 output도 이상하게 나올 확률이 높아진다는 것이다. 그렇게 떄문에, training시에 추론단의 input을 정담 label로 강제하는 기법이 있는데, 이를 teacher forcing이라고 한다.  

하지만 이는 실제 환경과 상이한 부분이 많다. 그렇기 때문에, 초반에 teacher forcing을 통해서 학습을 시키다가 후반부에는 정상적인 방식으로 학습을 시키는 방법을 사용한다.

#### how to calculate attention score
![image](https://user-images.githubusercontent.com/50571795/133968355-e6dedcc7-0ceb-48b9-9b77-e67e162f964a.png)


### Attention은?

- 기계번역(NMT)분야에서 성능을 굉장히 올려주었다.
  - decoder가 어떤 부분에 집중하고 있었는지 알 수 있다.
- 마지막 state의 vector만 사용했던 bottleneck을 해결했다.(기존엔 필연적으로 긴 문장에서 작동이 어려웠다.)
- gradient vanishing문제를 해결했다. (gradient를 encoding vector까지 바로 보낸다.)
- attention은 해석가능한 정보를 제공한다.
  - ![image](https://user-images.githubusercontent.com/50571795/133968928-e59f8381-dd5b-4203-bd5b-099d319be6de.png)
