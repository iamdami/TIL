import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from PIL import Image
import requests
from pycocotools.coco import COCO
import matplotlib.patches as patches


cocoAnnotationFilePath = "cocoapi/annotations/instances_val2017.json"
cocoAnnotation = COCO(annotation_file=cocoAnnotationFilePath)

cat_ids = cocoAnnotation.getCatIds()
category_ids = cocoAnnotation.getCatIds(['bicycle'])
# print(category_ids)

imgId = cocoAnnotation.getImgIds(catIds=[2])
# print(imgId[12:15])

annoId = cocoAnnotation.getAnnIds(imgIds=370208, catIds=[2])
# print(len(annoId))

annos = cocoAnnotation.loadAnns(annoId)

for anno in annos:
    print(anno['bbox'])

imageId = 42
imagePath = "cocoapi/images/train2017/"
imageName = str(imageId).zfill(12)+".jpg"
image = Image.open(imagePath+imageName)

fig, ax = plt.subplots()

for anno in annos:
    bbox = anno['bbox']
    bboxRec = patches.Rectangle((bbox[0], bbox[1]), bbox[2], bbox[3], linewidth=2, edgecolor="orange", facecolor="none")
    ax.add_patch(bboxRec)

ax.imshow(image)
plt.savefig(f"{imageId}_annotated.jpg", bbox_inches="tight", pad_inches=0)
plt.show()
