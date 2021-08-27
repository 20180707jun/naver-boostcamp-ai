# 3강 Dataset

![image](https://user-images.githubusercontent.com/50571795/130559336-71978155-f15c-4a8b-b1b0-0df5dd9c0516.png)  
오늘 수업은 Data Processing부분이다.

주어진 vanilla Data를 모델에서 적용할 수 있는 형태의 Dataset으로 바꿔야한다.

### Pre-processing
- 실제 현업에서는 noise가 많다.
  - ex) null, label제대로 되지 않은
- 따라서 전처리가 굉장히 중요함.
- Pre-processing이 전체과정의 80%에 해당할 정도이다.

#### Bounding box
- 불필요한 정보들은 box로 지운다.

#### Resize
- 계산의 효율을 위해 적당한 크기로 사이즈를 변경한다.

#### 도메인에 따라 다양한 case가 존재한다.
![image](https://user-images.githubusercontent.com/50571795/130569707-560a36d5-1916-4231-9282-dbfe0733c0d1.png)  
의료데이터에서는 이런식으로 전처리를 할 수 있다. 하지만 이렇게 전처리를 한 데이터를 이용해서 결과를 내야지 당위성을 얻을 수 있다.

## Generalization
- Bias, Variance
- Train/Validation
- Data Augmentation
- Augmentation 라이브러리

### Bias, variance
![image](https://user-images.githubusercontent.com/50571795/130571251-39df1d9f-98a0-4410-a9dc-696494a7d697.png)
- 정말 많이 보는 그림
- 학습이 너무 안 됐거나, 학습이 너무 잘 됐거나,

### train/validation
![image](https://user-images.githubusercontent.com/50571795/130571389-221dbbe4-6d9c-486b-87ab-60de2fe4d823.png)

### Data Augmentation
![image](https://user-images.githubusercontent.com/50571795/130571487-ff0e5a5f-c5fa-4dd3-97fa-8564afc6c64b.png)

좋은 libary
- torchvision.transforms![image](https://user-images.githubusercontent.com/50571795/130572061-fd2fee26-6ba3-421b-93db-ba85d4539b68.png)
- Albumentations : 더 빠르고 더 다양하다.

모든 것들은 여러가지 도구 가운데 하나이다.
여러가지 도구를 적용해보고 실험으로 증명해야 한다.

