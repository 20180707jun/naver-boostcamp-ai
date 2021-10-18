# MRC 1강

## MRC란?
MRC는 MachineReading Comprehension의 약자로 한글로 번역해보자면 기계독해이다. 주어진 지문을 이해하고, 주어진 질의의 답변을 추론하는 문제이다.

### MRC의 종류
- Extractive Answer Datasets : 질의에 대한 답이 항상 주어진 지문의 segment로 존재
- Descriptive/Narrative Answer Datasets : 답이 지문 내에서 추출한 span이 아니라, 질의를 보고 생성된 sentence의 형태 
- Multiple-choice Datasets : 질의에 대한 답을 여러 개의 answer candidates 중 하나로 고르는 형태


### Challneges in MRC
- 단어의 구성이 유사하지는 않지만 동일한 의미의 문장을 이해
- 대답할 수 없는 질문 : 지문에서 질문에 대한 답을 찾을 수 없을 때, 차라리 답이 없다라고 나와야함.
- Multi-hop reasoning : 여러 개의 document에서 질의에 대한 supporting fact를 찾아야지만 답을 찾을 수 있음

### MRC의 평가방법

- EM(Exact Match) : 예측한 답과 ground-truth가 정확히 일치하는 샘플의 비율
- F1 score : 예측한 답과 ground-truth 사이의 token overlap을 F1으로 계산

![image](https://user-images.githubusercontent.com/50571795/137650000-6c6b30f5-cd61-4bb2-ba0a-09a1577f4ab4.png)

- ROUGE-L : Ground-truth와 예측한 답 사이의 overlap을 계산
- BLEU(Bilingual Evaluation understudy) : 예측한 답과 ground-truth 사이의 precision

## Unicode & tokenization
### tokenizing
택스트를 토큰단위로 나누는 것.  
단어, 형태소, subword등 여러 토큰 기준이 사용된다.  

#### Subword 토크나이징
자주 쓰이는 글자 조합은 한 단위로 취급하고, 자주 쓰이지 않는 조합은 subword로 쪼갠다.  
"\#\#"은 디코딩ㅡㅇㄹ 할 때 해당 토큰을 앞 토큰에 띄어쓰기 없이 붙인다는 것을 뜻한다. 

#### BPE(Byte-Pair Encoding)
데이터 압축용으로 제안된 알고리즘.
NLP에서 토크나이징용으로 활발하게 사용되고 있다.
1. 가장 자주 나오는 글자 단위 Bigram(or Byte pair)를 다른 글자로 치환한다.
2. 치환된 글자를 저장해둔다.
3. 1~2번을 반복한다.  

![image](https://user-images.githubusercontent.com/50571795/137650204-04578fc4-d5bb-4f38-bb4b-a79012890528.png)

## KorQuAD란?
LG CNS가 AI 언어지능 연구를 위해 공개한 질의응답/기계독해 한국어 데이터셋  
인공지능이 한국어 질문에 대한답변을 하도록 필요한 학습 데이터셋
-  1,550개의 위키피디아 문서에 대해서 10,649건의 하위 문서들과 크라우드 소싱을 통해 제작한 63,952
개의 질의응답 쌍으로 구성되어 있음 (TRAIN60,407/DEV5,774/TEST3,898)
-  누구나 데이터를 내려받고,학습한 모델을 제출하고 공개된 리더보드에 평가를 받을 수 있음
è 객관적인 기준을 가진 연구 결과 공유가 가능해짐
-  현재 v1.0,v2.0공개:2.0은 보다 긴 분량의 문서가 포함되어 있으며,단순 자연어 문장 뿐 아니라 복잡한
표와 리스트 등을 포함하는 HTML 형태로 표현되어 있어 문서 전체 구조에 대한 이해가 필요

### 데이터 수집 과정
![image](https://user-images.githubusercontent.com/50571795/137650425-52c4233f-0e54-4372-8e2e-71c0f77e5f31.png)
