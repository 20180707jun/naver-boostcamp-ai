# 5강 모델
![image](https://user-images.githubusercontent.com/50571795/131077066-481261e2-8dd4-4bb7-9cd1-088c051fd32f.png)

### Desing Model with Pytorch
파이토치의 장점
- 자유롭고, 연구하기가 편하다.
- 연구와 공부에 있어서는 파이토치가 가장 좋다.
- **from research to production** 라는 슬로건이 있다.

파이토치
- low-level
  - low-level keras에 비해서 학습에 있어서 더 낮은 수준으로 구현하는 방식이기에, 중간 중간에 원하는 기능을 더 추가할 수 있다.
- Pythonic 
- Flexibility

### module
![image](https://user-images.githubusercontent.com/50571795/131086785-f9ed6767-6e79-44d7-a78a-0a22076efa60.png)

### forward
![image](https://user-images.githubusercontent.com/50571795/131087494-1dc07bb5-f80a-42f3-89d1-b0928a4c88e6.png)

### nn.Module Family
- nn.Module을 상속받은 모든 클래스의 공통된 특징
- 모든 nn.Module은 child modules를 가질 수 있다.
- 내 모델을 정희하는 순간, 그 모델에 연결된 모든 module을 확인할 수 있다. 

### Parameters
아래와 같이 parameter를 확인할 수 있다.
![image](https://user-images.githubusercontent.com/50571795/131088955-019beb8f-0e9f-45bf-a559-b2b653c0cb19.png)

### Pytorch의 Pythonic
- ![image](https://user-images.githubusercontent.com/50571795/131089871-e224bfb7-81fe-48ad-b9d7-32470461a809.png)그림과 같이 dicttype을 우리가 알기 때문에, 응용이 쉽다.