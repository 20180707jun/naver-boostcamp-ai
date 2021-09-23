# 6강 Beam Search and BLEU score

## 자연어 생성모델에서의 생성방법
크게 3가지가 있다.
- Greedy decoding
- Exhaustive search
- Beam search

### Greedy decoding
가장 확률이 높은 문장 1개를 계속 가지고 가는 방법이다.
1 문장만 가져가기 때문에, 그 모델에서 나온 global optimal인지 알 수 없고, 원하지 않는 단어가 나왔을 때, 뒤로 돌아갈 수가 없다.

### Exhaustive search
- ![image](https://user-images.githubusercontent.com/50571795/133974406-2dc6c1b5-f2da-449e-bbf1-0eb8a0d9d2ab.png)  
- 수식은 위와 같다. 
- 가능한 모든 sequence를 탐색하는 것이다.
- 최적의 해를 구할 수 있지만, cost가 너무 높다.
- vocabulary size가 V라고 할 때, O(V^t)의 시간복잡도가 나온다.

### Beam Search
- core idea : 매 step마다, k개의 최적의 선택지를 가지고 간다.(보통 k(beam size)는 5~10의 수)
- ![image](https://user-images.githubusercontent.com/50571795/133976319-b0d6e7e9-7df0-4e0a-b286-5ea79700074f.png)
- 그림으로 보면 다음과 같다.
![image](https://user-images.githubusercontent.com/50571795/133978585-f47dc4ec-a723-446f-a600-6f95403715c1.png)
- \<END> 토큰이 나오면 그 문장은 완성시켜두고, 이후로 4개씩 찾아나간다.
- 계속 진행한다면, 
  - time step T를  도달하거나,
  - 적어도 n개의 completed hypotheses를 만들어 낸다.(미리 정해둔 n)
- 최종 결정 방법
  - completed hypotheses 중에서 가장 높은 score를 뽑는다.
  - 하지만 길이가 길어지면 값이 작아지는 특징이 있기 때문에, hypotheses를 길이로 나누어준다.

## BLEU score
기존의 몇 가지 metric
- precision
- recall

![image](https://user-images.githubusercontent.com/50571795/133980080-2ee9f84d-bfee-40e1-a73d-22fe39d32b6d.png)

위의 metric들은 아래와 같은 문제를 가진다. model2는 gt와 순서가 완전히 다르지만 단어가 나온 빈도 수가 일치하기 때문에, 스코어가 100이 나왔다. 하지만 이는 적절하지 못한 수치이다.

그래서 나온 score가 바로 BLEU(BiLingual Evaluation understudy) score이다.  

![image](https://user-images.githubusercontent.com/50571795/133980160-1a6b4eff-7b8f-470c-a24a-2a04ba212874.png)

### BLEU score
- N-gram이라고 불리는 N개의 연속된 단어가 gt와 얼마나 겹치는가를 가지고 score를 계산한다.
- precision을 사용하고, recall을 무시한다.
  - e.g.)
  - GT : I lov this movie very much.
  - predict : 나는 이 영화를 많이 사랑한다.
  - 원래대로면 이 영화를 **정말** 많이 사랑한다. 가 되어야 하는데 **정말**이 빠져도 잘된 해석이다. 이러한 특징들 떄문에 recall을 사용하지 않고, precision을 사용한다.
  - 또 다른 이유는, 나는 노래를 많이 사랑한다. 가 되면 영화-> 노래가 되었기 떄문에, 완전히 다른 문장이고, 이를 metric이 낮게 평가해아하기 때문이다.

#### 계산방법
![image](https://user-images.githubusercontent.com/50571795/134016038-93d4785d-1385-452a-90e2-3ebba28bf7d1.png)  

작은 쪽에 가중치를 주기위해 기하평균을 사용했다.

![image](https://user-images.githubusercontent.com/50571795/133981256-ceafba9e-5f36-4bc8-baf8-ed1a73ff5248.png)
