# MRC 2강

## Extraction-based MRC
질문의 답벼빙 항상 주어진 지문 내에 span으로 존재.  
평가방법으로는 EM, F1 score가 사용된다.

f1score 계산 방법
![image](https://user-images.githubusercontent.com/50571795/137650561-dba7dfc6-ccd3-4ed8-9e39-1eb21abcbcfe.png)

구조는 다음과 같다.  

![image](https://user-images.githubusercontent.com/50571795/137650530-ca12dcb9-3ff2-4a99-8415-c862ca3c3352.png)


## Pre-processing
### Tokenization
텍스트를 작은 단위로 나누는 것
- 띄어쓰기 기준, 형태소, subword등 여러 단위 토큰 기준이 사용됨
- 최근엔 Out-Of_Vocabulary(OOV) 문제를 해결해주고 정보학적으로 이점을 가진 Byte Pair Encoding(BPE)를 주로 사용한다.
- 강의에서는 BPE 방법론 중 하나인 WordPiece Tokenizer를 사용한다.

```
# 예시
WordPiece Tokenizer사용 예시
“미국 군대 내 두번째로 높은 직위는 무엇인가?”
[‘미국’, ‘군대’, ‘내’, ‘두번째’, ‘##로’, 높은, ‘직’, ‘##위는’, ’무엇인가’, ‘?’]
```

### Attention mask
- 입력 시퀸스 중에서 attention을 연산할 때 무시할 토큰을 표시
- 0은 무시, 1은 연산에 포함
- 보통 \[PAD]와 같은 의미가 없는 특수 토큰을 무시하기 위해 사용한다.

### Token Type IDs
입력이 2개이상의 시퀸스 일 때, (질문+지문), 각각에게 ID를 부여하여 모델이 구분해서 해석하도록 유도

### 모델 출력값

정답은 문서내 존재하는 연속된 단어토큰(span)이므로, span의 시작과 끝 위치를 알면 정답을 맞출 수 있음.  
Extraction-based에선 답안을 생성하기 보다, 시작위치와 끝위치를 예측하도록 학습한다. 즉 Token Classification문제로 치환.  

![image](https://user-images.githubusercontent.com/50571795/137651230-03927ae7-c48c-4d17-b2a9-b9155ff4ab03.png)

### Fine-tuning

![image](https://user-images.githubusercontent.com/50571795/137651246-45bf9fe4-b6cb-41c1-8906-70d44613aa09.png)

![image](https://user-images.githubusercontent.com/50571795/137651300-d3f796d8-bc74-4c13-adea-46eb7ad06bcb.png)


구조는 위와 같다.

### Post-processing
다음과 같은 경우 candidate list에서 제거
- end position이 start position보다 앞에 있는 경우
- 예측한 위치가 context를 벗어난 경우
- 미리 설정한 max_answer_length보다 길이가 더 긴 경우

**최적의 답안 찾기**
1. Start/endpositionprediction에서 score(logits)가 가장 높은 N개를 각각 찾는다.
2. 불가능한 start/end조합을 제거한다.
3. 가능한 조합들을 score의 합이 큰 순서대로 정렬한다.
4. Score가 가장 큰 조합을 최종 예측으로 선정한다.
5. Top-k가 필요한 경우 차례대로 내보낸다.

