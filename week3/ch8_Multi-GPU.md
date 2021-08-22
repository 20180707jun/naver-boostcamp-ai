# 8강 Multi-GPU 학습

개념정리
- Sigle vs Multi
- GPU vs Node(System)
- Sgile Node Sigle GPU
- Sigle Node Multi GPU
- Multi Node Multi GPU

Model Parallel
- 다중 GPU에 학습ㅇ르 분산하는 두 가지 방법
  - 모델을 나누기
  - 데이터를 나누기
- 모델을 나누는 것은 생각보다 예전부터 썼음(alexnet)
- 모델의 병목, 파잎라인의 어려움 등으로 인해 모델 병렬화는 고난이도 과제

Data parallel
- 데이터를 나눠 GPU에 할당 후 결과의 평균을 취하는 방법
- minibatch 수식과 유사한데 한번에 여러 GPU에서 수행
- PyTorch에서는 아래 두가지 방식을 제공
  - DataParallel 
    - 단순히 데이터를 분배한 후 평균을 취함
    - GPU사용 불균형 문제 발생, Batch 사이즈 감소(한 GPU가 병목), GIL
  - DistributedDataparallel : 
    - 각 CPU마다 process를 생성하여 개별 GPU에 할당 
    - 기본적으로 DataParallel로 하나 개별적으로 연산의 평균을 냄

