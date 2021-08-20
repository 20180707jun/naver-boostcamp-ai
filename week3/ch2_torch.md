# 2강 PyTorch Basics

- torch는 np와 거의 비슷
- unsqueeze와 squeeze의 차이
- reshape 대신 view를 사용해라
- mm과 dot, matmul의 차이를 알아야 한다.

### formula
nn.functional모듈을 통해 다양한 연산을 지원한다.

- onehot
- cartesian product
- etc

## Autograd
```py
# ex
w = torch.tensor(2.0, requires_grad=True)
y = w**2
z= 10*y + 25
z.backward()
w.grad

# 40
```