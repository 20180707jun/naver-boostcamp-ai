# ResNeXt 요약


![image](https://user-images.githubusercontent.com/50571795/130902663-8f7bc3ea-d541-4d31-b9f7-061b136d8525.png)
개략적인 구조(왼쪽이 일반 ResNet, 오른쪽이 ResNeXt)

논문의 키워드 : cardinality

cardinality : the size of the set of transformations라고 되어있습니다.  
위의 그림에서 가로로있는 블록 1개가 1 cardinality라고 생각하시면 될 것 같습니다.

이러한 방식을 논문에서는 Grouped convolution이라고 부릅니다. VGGnet에서 GPU에서 한계로 인해 신경망의 채널 수를 두개로 쪼개서 연산하는 방식을 채용했는데, 아래의 그림과 서로 다른 특징에 대해서 학습을 하는 것을 볼 수 있었습니다. 이 부분을 차용한 것으로 보입니다.

![image](https://user-images.githubusercontent.com/50571795/130910404-ca90a1dc-74d2-4623-88e5-104209262a09.png)

### Increasing Cardinality vs Width
여기서 width는 채널 수를 의미한다. WRN(wid residual network)에서 모델의 width를 증가시키면 성능이 향상된다는 것을 밝혔습니다. 여기서는 cardinality가 늘어날수록 더 효율적임이 보입니다. 같은 parameter 수를 가지지만 성능이 더 낫다는 말이 됩니다..
![image](https://user-images.githubusercontent.com/50571795/130910999-ebf25fb4-2b28-47cb-aaab-a805f597d7be.png)

![image](https://user-images.githubusercontent.com/50571795/130911057-bc67266a-30b0-45c9-afa8-843b8981292e.png)

### Increasing cardinality vs Deeper/wider
깊이와 넓이를 증가시키는 것 보다 cardinality를 증가시키는 것이 효율적입니다.
![image](https://user-images.githubusercontent.com/50571795/130912135-2f475cc6-ce22-4dd7-83b1-c6a4a5a180e8.png)

### 실험에서는 어떻게 해야하는가?  
- 모델을 병렬적으로 돌리면 성능이 올라갈 것이다?
  - 자원은 어떻게 배분할 것인가?
