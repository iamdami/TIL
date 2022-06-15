import json
classes = ["Man","Monitor","Dog"]

def convert(size,box):
    x = box[0]
    y = box[1]
    w = box[2]
    h = box[3]
    return (x,y,w,h)

def convert_annotation(json_dir,destination_dir):
    with open(json_dir,'r') as f:
        data = json.load(f)
    for item in data['images']:
        image_id = item['id']      
        file_name = item['file_name']
        width = item['width']
        height = item['height']
        value = filter(lambda item1: item1['image_id'] == image_id,data['annotations'])
        outfile = open(destination_dir+"%s.txt"%(file_name[:-4]), 'a+')
        for item2 in value:
            category_id = item2['category_id']
            value1 = list(filter(lambda item3: item3['id'] == category_id,data['categories']))
            name = value1[0]['name']
            class_id = classes.index(name)
            box = item2['bbox']
            bb = convert((width,height),box)
            outfile.write(str(class_id)+" "+" ".join([str(a) for a in bb]) + '\n')
        outfile.close()
