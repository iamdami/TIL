def coco_to_csv(filename):

    import json

    # COCO2017/annotations/instances_val2017.json
    s = json.load(open(filename, 'r'))
    out_file = filename[:-5] + '.csv'
    out = open(out_file, 'w')
    #out.write('id,x1,y1,x2,y2,label\n')

    all_ids = []
    for im in s['images']:
        all_ids.append(im['id'])
    all_fn = []
    for im in s['images']:
        all_fn.append(im['file_name'])
    all_d = []
    for im in s['images']:
        all_d.append((im['height'],im['width']))

    classes=[]
    for cl in s['categories']:
        classes.append(cl['name'])

    all_ids_ann = []
    for ann in s['annotations']:
        image_id = ann['image_id']
        all_ids_ann.append(image_id)
        x1 = ann['bbox'][0]
        x2 =  ann['bbox'][2]-x1
        y1 = ann['bbox'][1]
        y2 =  ann['bbox'][3]-y1
        label = ann['category_id']
        out.write('{},{},{},{},{},{},{},{}\n'.format(classes[label], x1, y1, x2, y2,all_fn[image_id], all_d[image_id][1],all_d[image_id][0] ))
