# 10강 PyTorch Troubleshooting

## 공포의 단어 : OOM
해결하기 어려운 이유들...
- 왜 발생했는지 알기 어려움
- 어디서 발생했는지 알기 어려움
- Error backtracking 이 이상한데로 감
- 메모리의 이전상황의 파악이 어려움

### 해결방법
1. Batch Size를 줄인다.
2. GPU clean
3. Run

#### GPUUtil 사용하기
- nvidia-smi처럼 GPU의 상태를 보여주는 모듈
- Colab은 환경에서 GPU상태 보여주기 편함
- iter 마다 메모리가 늘어나는지 확인!!!
```py
!pip install GPUitl
import GPUtil
GPUtil.showUtilization()
```
### torch.cuda.empty_cache() 써보기
- 사용되지 않은 GPU상 cache를 정리
- 가용 메모리를 확보
- del과는 구분이 필요
- reset 대신 쓰기 좋은 함수
- loop이 시작되기 전에 한번 사용하면 좋다!!!


### trainning loop에 tensor로 축적되는 변수는 확인할 것
- tensor로 처리된 변수는 GPU상에 메모리 사용
- 해당 변수 loop 안에 연산이 있을 때 GPU에 computational graph를 생성(메모리 잠식)

### del 명령어를 적절히 사용하기
- 필요가 없어진 변수는 적절한 삭제가 필요함
- python의 메모리 배치 특성상 loop이 끝나도 메모리를 차지함.

### 가능 batch 사이즈 실험해보기
- 학습시 OOM이 발생했따면 batch 사이즈를 1로 해서 실험해보기

### torch.no_grad()사용하기
- inference 시점에서는 torch.no_grad()구문을 사용
- backwrad pass 으로 인해 쌓이는 메모리에서 자유로움

**이 밖에도 예상할 수 없는 에러들이 많다!!**
