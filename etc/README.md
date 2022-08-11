### .m file
- An M file is a text file used by MATLAB, an application used for mathematical computations. It can store a script, class, or an individual function in the MATLAB language. M files are used for executing algorithms, plotting graphs, and performing other mathematical operations.  
<br>

### .pyx file
- Source code file written in Pyrex, a Python-like language used for writing Python extension modules with C-like syntax; may contain references to existing C modules; compiles code that increases the execution time of Python programs.  
<br>

### installing scikit-image
- version check from Python shell or Jupyter notebook  
```
import skimage
print(skimage.__version__)
```
- version check from the command line  
```
python -c "import skimage; print(skimage.__version__)"
```
(Try python3 if python is unsuccessful.)  
<br>

- Installation via pip  
```
# Update pip
python -m pip install -U pip
# Install scikit-image
python -m pip install -U scikit-image
```
<br>

### coco api
- [pycocoDemo.ipynb](https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocoDemo.ipynb)  
<br>

### ref.
- [detectron2 evaluation coco_evaluation](https://detectron2.readthedocs.io/en/latest/_modules/detectron2/evaluation/coco_evaluation.html)  
