0830 회의

base model은 efficientnet_b1으로 통일

화요일 저녁까지 성능을 내고
성능을 낸사람 기준으로 baseline작성 및 코드 취합

수요일~ 앙상블코드 작성

제출할 때 18 class에 대한 분포도로 eval set과 어느정도로 유사한지 확인 후 제출


하겸님:
mtcnn으로 crop해서 사용하고 있음. 이렇게 하다보니 용량이 미리 줄어서 시간을 획기적으로 줄일 수 있게됨.

에폭은 6번이면 충분하다.

작은 모델 작은 에폭으로 분포를 비슷하게 맞춰보자.

adam은 2~3번이면 

sgd 7~11번 0.0001기준


efficientnet_b1



gender, age, mask set1 regnet
set2 efficientnet_b1


------
8/30 회의록
- 다영 : eval 하는 것이기 때문에 성능을 어떻게 넣어보아야 할까?
- 하겸 : 언제까지로 하는 것이 좋을까?
- 


할일
- f1 score수정
- tag 고치기
- 로그에서 tag 확인해서 어떤 부분이 어떻게 문제인지 판별
- mask 부분이 문제라면 따로 모델링 후 합치기

부족했던점
- validation에 대해서 학습을 진행하지 않음
- flip 사용x


해보고 싶은것 grad cam으로 어디를 잡는지 확인해보고 싶다. 
age를 mask와 not-mask로 확인하고 있는데, 이렇게 되면 mask부분에 대해서 feature를 못잡고 있지 않을까 생각이든다.