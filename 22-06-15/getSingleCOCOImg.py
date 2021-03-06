from pycocotools.coco import COCO
import requests

coco = COCO('cocoapi/annotations/instances_train2017.json')
cats = coco.loadCats(coco.getCatIds())
nms=[cat['name'] for cat in cats]
print('COCO categories: \n{}\n'.format(' '.join(nms)))

catIds = coco.getCatIds(catNms=['person'])
imgIds = coco.getImgIds(catIds=catIds )
images = coco.loadImgs(imgIds)
print("imgIds: ", imgIds)
print("images: ", images)

for im in images:
print("im: ", im)
img_data = requests.get(im['coco_url']).content
with open('downloaded_images/' + im['file_name'], 'wb') as handler:
handler.write(img_data)
