### COCO dataset
- [COCO data format](https://comlini8-8.tistory.com/67)  
- JSON file(크게 5가지로 정보 구분됨)    
  - Info  
    - verision of dataset, details, created date etc..(high level informations)
  - Licences  
    - Licence list of the image  
  - Image  
    - dataset에 속하는 Total image list  
    - image 각각의 file name, width, height etc..   
  - categories  
    - dataset에 존재하는 category에 대한 information(id, name)
  - Annotation  
    - annotations ['Images']는 이미지 id당 한 개의 dict만 존재하지만,    
      annoatations['annotations']는 이미지 id 당 여러 개(이미지에 담긴 객체 수만큼) dict 존재
- pycocotools
  - https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/coco.py  
```
from pycocotools.coco import COCO
coco = COCO('.json')
```
<br>
- [COCO json file 깔끔하게 보기@@](https://velog.io/@dkdk6638/Pytorch-COCO-Dataset)  
- https://stedolan.github.io/jq/  
<br>

응 lfw seminar 괘망함,,,,,,,구치만 괜찮아 하면 할 수 있는 고~~~  
