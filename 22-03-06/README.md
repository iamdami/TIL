torch.squeeze
===
- https://pytorch.org/docs/stable/generated/torch.squeeze.html  
- https://sanghyu.tistory.com/86  
<br>

```torch.squeeze(input, dim=None, *, out=None) → Tensor```

Returns a tensor with all the dimensions of input of size 1 removed.  
<br>

For example, if input is of shape: (A \times 1 \times B \times C \times 1 \times D)(A×1×B×C×1×D) then the out tensor will be of shape: (A \times B \times C \times D)(A×B×C×D).

When dim is given, a squeeze operation is done only in the given dimension. If input is of shape: (A \times 1 \times B)(A×1×B), squeeze(input, 0) leaves the tensor unchanged, but squeeze(input, 1) will squeeze the tensor to the shape (A \times B)(A×B).  
<br>

### parameters
- input (Tensor) – the input tensor.
- dim (int, optional) – if given, the input will be squeezed only in this dimension

<br>

### example
```
>>> x = torch.zeros(2, 1, 2, 1, 2)
>>> x.size()
torch.Size([2, 1, 2, 1, 2])
>>> y = torch.squeeze(x)
>>> y.size()
torch.Size([2, 2, 2])
>>> y = torch.squeeze(x, 0)
>>> y.size()
torch.Size([2, 1, 2, 1, 2])
>>> y = torch.squeeze(x, 1)
>>> y.size()
torch.Size([2, 2, 1, 2])
```
<br>

## squeeze()
- squeeze 함수는 차원이 1인 차원 제거해줌  
- 따로 차원을 설정하지 않으면 1인 차원 모두 제거  
- 차원을 설정해주면 그 차원만 제거  
<br>

```
import torch

x = torch.rand(3, 1, 20, 128)
x = x.squeeze() #[3, 1, 20, 128] -> [3, 20, 128]
```
<br>

*batch가 1일 때 batch 차원도 없애버리는 경우가 생길 수 있음  
<br>

```
import torch

x = torch.rand(1, 1, 20, 128)
x = x.squeeze() # [1, 1, 20, 128] -> [20, 128]

x2 = torch.rand(1, 1, 20, 128)
x2 = x2.squeeze(dim=1) # [1, 1, 20, 128] -> [1, 20, 128]
```
<br>

## unsqueeze()
unsqueeze 함수는 squeeze 함수와 반대로 1인 차원을 생성하는 함수  
-> 어느 차원 1인 차원을 생성할 지 꼭 지정해 주어야함  
<br>

```
import torch

x = torch.rand(3, 20, 128)
x = x.unsqueeze(dim=1) #[3, 20, 128] -> [3, 1, 20, 128]
```
