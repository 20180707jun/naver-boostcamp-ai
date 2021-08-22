# Enriching Word Vectors with Subword Information (Fast Text)

## 요약
- w2v 모델과 작동방식은 같다.
- 다만 차이점은 기존 w2v는 단어 단위로 벡터화를 하다보니, 단어가 비슷한 것들에 대해서 학습이 약했다.
- 또한 oov(out of vocabulary)를 해결하지 못했다.
- 하지만 논문에서 얘기하는 sisg(Subword Information Skip Gram)은 이러한 문제에 강했다.

### 학습방식
- 논문에서의 예시를 참고
- where라는 단어에 대해서 n을 3을 주고, 학습을 시킨다면,
- <wh, whe, her, ere, re>로 나뉜다.
- 꺽쇠는 시작과 끝에 붙인다. 이는 \<her>과 gram으로 나뉜 her를 구별할 수 있게 해준다.
- 이렇게 학습된 gram vector들의 합으로 word vector를 구하게 된다.
- 이러한 방식은 적은 데이터에서도 더 많은 학습데이터를 갖게되고, 따라서 적은데이터에서 성능이 기존 w2v보다 더 잘나오게 된다.
- 합성어가 많은 언어에서 기존 모델보다 성능향상이 크다.

예를 들면 eat, eats, eating과 같은 단어들을 기존보다 더 잘 표현할 수 있다.
x축은 oov인데도 불구하고 표현이 되는 것을 알 수 있다.
![image](https://user-images.githubusercontent.com/50571795/130005840-819c22ab-8313-4985-99a6-c43f4e3df70a.png)

![image](https://user-images.githubusercontent.com/50571795/130006051-7b0d6686-94b9-40ab-83e4-c080e18aea1a.png)
