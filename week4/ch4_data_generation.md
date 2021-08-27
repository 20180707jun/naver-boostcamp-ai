# 4강 Data Generation

## Data Feeding
### Generator
![image](https://user-images.githubusercontent.com/50571795/130590370-92f5e711-a306-4f42-a4c0-a13f9bfa7b4c.png)  
generator가 model에 속도를 맞춰줘야지 가장 효율적으로 학습이 가능하다.  
![image](https://user-images.githubusercontent.com/50571795/130591441-3d37c28b-717c-4042-86e7-ae580198eb38.png)
어떻게 tranform하느냐에 따라 속도가 달라지는 것을 볼 수 있다.
## torch.utils.data
- Dataset
- DataLoader

### Dataset

```py
# 큰 틀은 이렇다.
from torch.utils.data import Dataset

class MyDataset(Dataset):
    def __init__(self):
        pass
    
    def __getitem__(self, index):
        return None
    
    def __len__(self):
        return None
```
```py
# 아래의 예시와 같이 내가 만든 Dataset을 효율적으로 사용할 수 있도록 관련 기능 추가
train_load = torch.utils.data.DataLoader(
    train_set,
    batch_size=batch_size,
    nu9m_workers=num_workers,
    drop_last=True,
)
```

torch.utils.data.DataLoader에는 엄청 다양한 기능이 많다.  
![image](https://user-images.githubusercontent.com/50571795/130594869-9604621e-7827-4ebd-91f1-f7f39877cb67.png)  
위와 같이 옵션을 줌으로써 좀더 빠르게 돌릴 수 있다. 

![image](https://user-images.githubusercontent.com/50571795/130595454-15cbf3f2-1b69-4a03-a37c-cb516fab292d.png)  
위의 예시처럼 dataset과 dataloader는 엄연히 하는 일이 다르다.
위와 같이 코드를 작성한다면, dataloader는 1개만 만들면 된다. 
dataset을 제대로 만들자!!
