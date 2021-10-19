# MRC 3강

## Generation-based MRC
MRC 문제를 푸는 방법
1. Extraction-based mrc : 지문 내 답의 위치를 예측 -> 분류문제
2. Generation-based mrc : 주어진 지문과 질의를 보고, 답변을 생성 -> 생성문제

평가 방법은 EM, F1 Score로 기존의 extract모델과 다르지 않다.

![image](https://user-images.githubusercontent.com/50571795/137651673-1db523ee-b12f-43ab-864b-12381e4bed41.png)  

구조는 위와 같다.

## Pre-processing
```
WordPiece Tokenizer

질문: '미국 군대 내 두번째로 높은 직위는 무엇인가?’,
토큰화된 질문: ['미국', '군대', '내', '두번째', '##로', '높은', '직', '##위는', '무엇인가', '?']
인덱스로 바뀐 질문: [101, 23545, 8910, 14423, 8996, 9102, 48506, 11261, 55600, 9707,
19855, 11018, 9294, 119137, 12030, 11287, 136, 102]
```

인덱스로 바뀐 질문을 보통 input_ids(또는 input_token_ids)로 부른다.  
모델의 기본 입력은 input_ids만 필요하나, 그 외 추가적인 정보가 필요함.

### 입력 표현 - Special Token
학습 시에만 사용되며 단어 자체의 의미는 가지지 않는 특별한 토큰
- SOS(start of Sentence), EOS(End of Sentence), CLS, SEP, PAD, UNK 등등
- Extration-based MRC에선 CLS, SEP, PAD 토큰을 사용
- Generation-based MRC에서도 PAD토큰은 사용됨. CLS,SEP토큰 또한 사용할 수 있으나, 대신 자연
어를 이용하여 정해진 텍스트 포맷(format)으로 데이터를 생성

![image](https://user-images.githubusercontent.com/50571795/137658626-4f28fddd-5bbe-47e2-8fc5-481e78b449ce.png)

### 입력 표현 - additional information

Attention mask
- Extracktion-based MRC와 똑같이 어텐션 연산을 수행을 결정하는 어텐션 마스크 존재

Token type ids
- BERT와 달리 BART에서는 입력시퀸스에 대한 구분이 없어 token_type_ids가 존재하지 않음
- 따라서 Extraction-basesd MRC와 달리 입력에 token_type_ids가 들어가지 않음

![image](https://user-images.githubusercontent.com/50571795/137658772-b012382f-fc25-465c-83a5-744c27c353b4.png)

### 출력 표현 - 정답 출력
Sequence of token ids
- Extraction-based MRC에선 텍스트를 생성해내는 대신 시작/끝 토큰의 위치를 출력하는것이 모델의 최종 목표였음
- Generation-based MRC는 그보다 조금 더 어려운 실제 텍스트를 생성하는 과제를 수행
- 전체 시퀸스의 각 위치마다 모델이 아는 모든 단어들 중 하나의 단어를 맞추는 classification을 문제

