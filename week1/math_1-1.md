# 행렬은 뭔가요?

![image](https://user-images.githubusercontent.com/50571795/128105440-e9ed4a35-6e64-40fd-9679-54dbc3e2789e.png)
- 대문자는 행렬, 볼드체 백터


### 전치행렬
![image](https://user-images.githubusercontent.com/50571795/128105651-4b90dd66-682d-4797-87db-b5e1267cf7bd.png)

### numpy inner
- numpy matrix inner는 다르다.

![image](https://user-images.githubusercontent.com/50571795/128106032-122ef2ea-856d-4060-a37f-59db350f1e56.png)

### 행렬을 이해하는 방법
![image](https://user-images.githubusercontent.com/50571795/128106186-73173d20-9762-4b5b-bcc3-5989eb659f36.png)

### 역행렬 이해하기
![image](https://user-images.githubusercontent.com/50571795/128106304-410cf37c-d278-4998-bf81-62bf068273d4.png)

- 만일 역행렬을 계산할 수 없다면 유사역행렬(pseudo-inverse) 또는 무어-펜로즈(Moore-Penrose) 역행렬을 이용한다.(A+ = 무어펜로즈역행렬)
![image](https://user-images.githubusercontent.com/50571795/128106682-ba2b5a01-f5a5-46d4-a51d-20d5378739ce.png)

### 응용1 : 연립방정식 풀기
- ```np.linalg.pinv```를 이용하여 연립방정식의 해를 구할 수 있다.

### 응용2 : 선형회귀분석
- nplinalg.pinv를 이용하여 데이터를 선형모델로 해석하는 선형 회귀식을 찾을 수 있다.  

![image](https://user-images.githubusercontent.com/50571795/128109151-97657e4b-c246-4f70-b0f6-c001e1f083f4.png)  

![image](https://user-images.githubusercontent.com/50571795/128109223-d6faeb67-44fb-4a76-bcc3-df18c482e7b0.png)
