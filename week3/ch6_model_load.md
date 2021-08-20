# 6강 모델 불러오기
- 요즘은 기존에 학습된 큰 모델을 가져와서 사용하는 것이 일반적이다.
- 이를 위해서 몇 가지 알아야할 것들이 있다.
  - model.save
  - checkpoint

## Transofer learning
- 위에서 말한 다른 큰 모델을 가져와서 학습하는 기법이다.
- 요즘 DL문제를 해결하는데에 있어서 가장 일반적이다.
- backbone architecture가 잘 학습된 모델에서 일부분만 변경하여 학습을 수행한다.
- torchVision에서 다양한 것들을 제공
- NLP에서는 HuggingFace가 사실상 표준이다.

![image](https://user-images.githubusercontent.com/50571795/130011178-fe20324c-34e1-4c9c-8a42-91c5dd96fe07.png)  
위의 그림과 같이 backbone layer는 freezing시켜서 사용한다.