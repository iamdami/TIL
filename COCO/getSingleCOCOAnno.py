with open('annotations_download_' + classes + '.csv', mode='w', newline='') as annot:
for im in images:
annIds = coco.getAnnIds(imgIds=im['id'], catIds=catIds, iscrowd=None)
anns = coco.loadAnns(annIds)
for i in range(len(anns)):
annot_writer = csv.writer(annot)
#annot_writer.writerow([im['coco_url'], anns[i]['bbox'][0], anns[i]['bbox'][1], anns[i]['bbox'][0] + anns[i]['bbox'][2], anns[i]['bbox'][1] + anns[i]['bbox'][3], classes])
annot_writer.writerow(['downloaded_images/' + im['file_name'], int(round(anns[i]['bbox'][0])), int(round(anns[i]['bbox'][1])), int(round(anns[i]['bbox'][0] + anns[i]['bbox'][2])), int(round(anns[i]['bbox'][1] + anns[i]['bbox'][3])), classes])
#print("anns: ", im['coco_url'], anns[i]['bbox'][0], anns[i]['bbox'][1], anns[i]['bbox'][0] + anns[i]['bbox'][2], anns[i]['bbox'][1] + anns[i]['bbox'][3], 'person')
annot.close()
