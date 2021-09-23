# 3강 RNN
RNN의 구조는 다음과 같다.  
![image](https://user-images.githubusercontent.com/50571795/133278849-1318ad35-8589-4b59-9614-35da08b5f93e.png)  
같은 구조를 반복하는 구조이다.

notation은 아래와 같다.  
![image](https://user-images.githubusercontent.com/50571795/133279460-3b912318-417b-4166-9608-50b53eb073a2.png)


## Types of RNNs
![image](https://user-images.githubusercontent.com/50571795/133279843-a859364a-b536-47de-b79a-ec67131a2d10.png)
- One-to-one : Stadard Neural Networks
- One-to-many : Image Captioning
- Many-to-one : Sentiment Classification
- Sequence-to-sequence : Machine Translation

## Character-level Language Model
![image](https://user-images.githubusercontent.com/50571795/133280698-374af45b-44e7-4940-a101-09738ff2a97e.png)

### BPTT(Backpropagation through time)
![image](https://user-images.githubusercontent.com/50571795/133716972-3278bfae-898a-427c-8131-87386d416da4.png)
- 그림은 위와 같다. 
- 아직 잘 이해가 안간다.

#### How RNN works
![image](https://user-images.githubusercontent.com/50571795/133717071-45604acd-aaf4-45b7-a73d-fb45754b57c6.png)  
![image](https://user-images.githubusercontent.com/50571795/133717099-f2141a17-4ca3-4886-9f95-944409473b0e.png)
- output vector의 특정 행의 원소를 확인해보면 이런 식으로 볼 수 있다.

#### RNN is Excellenct, but...
- 백프롭 시에, 같은 메트릭스를 여러번 곱하기 때문에, gradient vanishing 또는 exploding문제가 생긴다.
- ![image](https://user-images.githubusercontent.com/50571795/133717498-aa7085c8-224e-4f5c-a486-0cf1711778a9.png)




빔서치는 인코딩된 정보를 가지고 디코딩 할때, 적합한 단어를 찾는 기법중에 하나이다.

처음엔 그리디 디코딩이다.
각 단계에서 가장 적합한 단어를 취합니다.
문제는 틀렸을 ㅅ ㅣ 돌아갈 수 없습니다. 

이를 해결 하기 위해서 나온 것이

Exhaustive search decoding
brute force와 비슷한 방법론
몯느 경우를 다계산하여 가장 노은 p를 취하여 해결한다.
하지만 모든 경우를 선택하기에는 코스트가 너무 높다.

빔 서치 디코딩
k=1일 떈 greedy decoding

k개의 hypothesis를 정해서 그것을 따라간다. 

질문 마지막에 end가 나올때 몇개를 갖고가는가?

at fault

recall 1/10
precision 1/10

