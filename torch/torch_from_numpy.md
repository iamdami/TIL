- [torch.from_numpy](https://pytorch.org/docs/stable/generated/torch.from_numpy.html#torch-from-numpy)  
  - ```torch.from_numpy(ndarray) → Tensor```  
  - Creates a Tensor from a numpy.ndarray  
  - The returned tensor and ndarray share the same memory  
  - Modifications to the tensor will be reflected in the ndarray and vice versa  
  - The returned tensor is not resizable  
```
>>> a = numpy.array([1, 2, 3])
>>> t = torch.from_numpy(a)
>>> t
tensor([ 1,  2,  3])
>>> t[0] = -1
>>> a
array([-1,  2,  3])
```
<br>

