# 2강 Word Embedding

- 단어를 vector로 표현하는 기법
- cat과 kitty는 비슷한 단어이므로 비슷한 vector로 나타남.(= 거리가 가까움)
- hamburger와 cat은 가깝지 않다.

## Word2Vec
주변단어들은 의미가 비슷하다라는 전제한다.  
![image](https://user-images.githubusercontent.com/50571795/132268761-bb808cb8-2e5c-4844-b5eb-64c2ca6021fc.png)  
cat 주변에 나타나는 단어들의 확률분포를 학습

### w2v 학습방식
1. word를 tokenizing
2. 유의미한 단어들을 모아서 사전을 구축
3. 단어를 one-hot vector로 나타냄.
4. sliding window기법으로 (input, output)쌍을 만든다.
5. 후에 output = softmax(W_2\*W_1\*input) 형태의 식을 계산
6. W_1의 벡터들을 embedding vector 사용

![image](https://user-images.githubusercontent.com/50571795/132286178-f3211187-dbc5-400d-9f7f-340dddbf371b.png)



#### w2v 특징 1

![image](https://user-images.githubusercontent.com/50571795/132286399-936d1c26-60bd-4e4e-bfcc-dc1ecb029f11.png)

위의 그림과 같이 vector로 나타낸 점들이 해당 단어들의 실제 관계를 벡터공간에서 나타내게된다.

![image](https://user-images.githubusercontent.com/50571795/132286570-cd008100-c90c-4848-8a6a-17c175beccc6.png)
#### w2v 특징 2
Word instrusion detection에 사용되어 질 수 있다. 단어가 주어졌을 때 나머지 단어들과 의미가 가장 상이한 단어를 찾는 task이다.  
![image](https://user-images.githubusercontent.com/50571795/132286661-c90a7333-4730-4058-bca4-2156a5aee162.png)  
방식은 다음과 같다.
- 각 단어들의 embedding vector를 구한다.
- 각 단어들의 embedding vecdtor로부터 다른 단어들과의 Euclidean Distance를 구하여 평균을 낸다.
- 이 평균 거리가 가장 큰 단어가 찾아야할 단어가 된다.

### Application of w2v
대부분의 NLP task에서 사용되고 있다.
- Word similarity
- Machine translation
- Part-of-speech (PoS) tagging
- Named entity recognition (NER)
- Sentiment analysis
- Clustering
- Semantic lexicon building

## GloVe (Global Vectors for Word Representation)
[wiki docs 참고](https://wikidocs.net/22885)
- w2v과 더불어 많이 쓰이는 word embedding 방법론
- 기존의 방법론(w2v, LSA)를 비판하면서 나온 방법론
- LSA는 카운트 기반으로 코퍼스의 전체적은 통계 정보를 고려하기는 하지만, 왕:남자 = 여왕 :? 과 같은 단어 유추 작업에서는 성능이 떨어진다.
- 반면에 w2v는 이러한 단어 유추 문제에서는 성능이 괜찮지만, 윈도우사이즈만을 고려하기 때문에 코퍼스의 전체적인 통계 정보를 반영하지는 못한다.
- GloVe는 LSA의 카운트 기반의 방법과 w2v의 예측 기반의 방법론 두가지를 모두 사용
- 트레이닝이 빠르고, 작은 코퍼스에서도 잘 작동한다.  
- 수식은 다음과 같다.
![image](https://user-images.githubusercontent.com/50571795/132298273-3003f486-fb76-44c0-a138-06b13f22281e.png)
