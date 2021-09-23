# 9강 Self-Supervised Pre-Training Models
- GPT-1
- BERT

## 최근동향
- Transformer 모델과 self-attention block이 범용적인 encoder와 decoder가 되었다.
- 최근에는 이 self-attention block을 더 많이 쌓아서 self-supervised learning framework로 transfer learning을 하여 fine tuning하여 사용하고 있다.
- 다른 분야에서도 self-attention이 사용되어진다. 
  - e.g., recommender systems, drug discovery, computer vision, ...

## GPT-1

![image](https://user-images.githubusercontent.com/50571795/133367365-aa6b4293-a340-47f0-8ca4-feb0bfbd51f0.png)
- 12개의 self-attention block으로 이루어져있다.
- 4가지 task를 수행한다.
  - Classification
    - EOS 대신 Extract를 입력벡터로 주어 문장이 긍정인지 부정인지 예측 하는 task
  - Entailment
    - 함의 : 문장 A가 사실일 때, 문장 B의 사실을 보장하는 것, 가설이 참인지 맞추는 task
    - e.g.,
    - 어제 존이 결혼했다. (premise)
    - 어제 한 커플은 결혼했다. (hypothesis)
    - 두 단어 사이에 Delimiter를 넣는다.
  - Similarity
    - 유사도를 측정하는 task
  - Multiple Choice
- 이를 transfer learning에 활용할 때는 아래의 그림과 같이 linear부분을 떼어내 버리고, 단어에 대한 encoder vector를 사용하게 된다.
  - ![image](https://user-images.githubusercontent.com/50571795/133370660-828b1158-a025-45e5-a6ad-33a3d85bb387.png)

#### Experimental Results
![image](https://user-images.githubusercontent.com/50571795/133370932-3333f3ce-ac2c-4bc5-881e-5eda345960c6.png)
- 일반적으로 더 좋은 결과를 내는 것을 알 수가 있다.

## BERT
- 현재 가장 널리 쓰이는 pre-trained model
- masked languaged modeling task로 학습
- Use large-scale data and large-scale model

![image](https://user-images.githubusercontent.com/50571795/133371485-414fbbfc-a3cc-482a-8f0f-96338122394b.png)

- GPT-1 은 \<SOS> I study math.를 학습한다고 할 때, 앞에서 부터 순차적으로 진행하였다.
  - ![image](https://user-images.githubusercontent.com/50571795/133371668-36953bc6-c9f4-4505-8eb0-b9bd19d68209.png)

### Pre-training Task in BERT
- Masked Language Model(MLM)
  - 어떠한 문장이 주어졌을 때, 확률적으로 mask로 치환하여 맞추는 task를 수행한다.
- 다음에 오는 문장이 적절한 문장인지 아닌지 찾는 task (binary classification)
  - ![image](https://user-images.githubusercontent.com/50571795/133375172-fbe3cf4a-1a6c-4f47-97f1-cb535e90b63b.png)



#### Problem
- pre-trained모델이 15%가 mask로 나오는 문서로 train된다.
  - 이는 분류 task등 다른 downstream task를 수행할 때 문제가 될 수 있다.
  
#### Solution
- mask해야하는 단어들 중에,
  - 80%는 mask로,
  - 10%는 다른 임의의 단어로, e.g., I love this movie -> i him ths movie
    - 해당 단어를 원래 있어야 하는 단어로 복원하는 task(더 어렵다.)
  - 10%는 단어를 바꾸지 않고, 그대로 둔 체, 그 단어가 다른 단어로 바뀌어야 하는지 -> 소신있게 예측하게 된다.
  
#### BERT Summary
1. Model Architecture(L : self-attention block, A : Attention head 수, H : encoding vector 차원 수)
  - BERT BASE : L = 12, H = 768, A = 12
  - BERT LARGE : L = 24, H = 1024, A = 16
2. Input Representation
  - WordPiece Embeddings (30,000 WordPiece) 워드를 더 잘게 쪼개서 subword로 만들어서 embedding e.g., pre-training -> pre, training
  - learned positional embedding // 어떤 뜻인지 잘 모르겠습니다.
  - \[CLS]- Classification embedding
  - Packed sentence embedding \[SEP] : 문장 끝에 나타나는 토큰
  - Segment embedding
3. Pre-training Task
  - Masked LM
  - Next Sentence Prediction
    - 아래 그림의 he는 두 번쨰 문장의 첫 번째로 오는 단어로 다른 표기를 해줄 필요가 있다. 그 것을 segment embedding을 통해서 정보를 준다.
    - ![image](https://user-images.githubusercontent.com/50571795/133378798-49fa9914-28df-44f8-b9dc-458ff7e2392c.png)

  
### BERT : Fine-tuning Process
[블로그](https://vanche.github.io/NLP_Pretrained_Model_BERT(2)/) 참고
![image](https://user-images.githubusercontent.com/50571795/133379236-54ca0440-ac47-4033-ae2d-7f2f3aca4aa6.png)
- (a) Sentence Pair Classification Tasks : Sentence pair에 대해서 classification, 모순관계 또는 내포관계를 확인
  - MNLI(Multi-Genre Natural language Inference) : 
  - QQP(Quora Question Pairs): Quora에 올라온 질문 페어가 의미적으로 동일한지 확인하는 테스크
  - QNLI(Question Natural language inference): SQuAD의 이진 분류 버전. paragraph가 answer를 포함하는지 안하는지를 확인하는 문제
  - SST-2(Stanford Sentiment Treebank) : 단문장 이진분류 문제
  - CoLA(Corpus of Linguistic Acceptability): 영어문장이 언어학적으로 acceptable한지 확인하는 이진분류문제

## BERT vs GPT-1

- Training-data size
  - 2500M(BERT) vs 800M(GPT-1)
- Training special tokens during training
  - BERT learns \[SEP],\[CLS] and sentence A/B
- Batch size
  - BERT 128,000words vs GPT 32,000 words
  - 일반적으로 batch가 커지면 모델 성능 좋아지고, 학습이 안정화 되는 경향이 있다.
- GPT에서는 learning rate을 모든 task에서 동일, BERT는 다 다르게 수행함.

#### GLUE Benchmark Results
![image](https://user-images.githubusercontent.com/50571795/133381527-69a52407-c609-4f38-8442-e4c6b1a4976a.png)

### BERT fine tune으로 성능을 많이 올릴 수 있는 task
#### MRC(Machine Reading Comprehension) Task

SQuAD 1.1(Stanford Question Answering Dataset)  
![image](https://user-images.githubusercontent.com/50571795/133382390-808419a2-88a1-4004-9e9e-dcc39262c939.png)
- 질문과 지문을 concat하여 SEP토큰을 통해서 encoding을 진행
- encoding vector FC layer를 태운다.
- 전체 concat된 문장에 대해서 해당 과정을 수행하여, 빈칸에 해당하는 첫 번째 단어를 softmax를 통해 맞추려고 한다.
- 끝나는 시점도 예측해야한다. 마찬가지로 concat된 전체 문장에 대해서 해당 과정을 수행한다.

SQuAD 2.0
- 1.1 버전에서 답이 없는 경우도 존재한다.
- 답이 있는지 없는지 판별 -> 답이 있으면 위의 task 수행
- CLS토큰을 이용하여 no answer를 맞춘다.

SWAG  
![image](https://user-images.githubusercontent.com/50571795/133383668-847c8030-61aa-4a0b-a609-c1bf22e783d1.png)
- 위의 그림과 같이 다음 문장을 예측하는 task
- 1 번 문장과 concat 하여 cls 이 것을 n번 반복한다.


#### Big model help a lot
![image](https://user-images.githubusercontent.com/50571795/133383929-12578164-1713-4eed-9811-3a4a61fa3710.png)  
위의 그림과 같이 parameter 수를 늘릴 때 성능이 더 좋아지는 것을 알 수가 있었다.