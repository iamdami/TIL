import os
import glob
import pandas as pd

def yolo_to_csv(yolo_dir,destination_dir):
    os.chdir(yolo_dir)
    myFiles = glob.glob('*.txt')
    classes=[]
    with open(yolo_dir+'/classes.names','rt') as f:
        for l in f.readlines():
            classes.append(l[:-1])

    width=1024
    height=1024
    image_id=0
    final_df=[]
    for item in myFiles:


        image_id+=1
        with open(item, 'rt') as fd:
            for line in fd.readlines():
                row = []
                bbox_temp = []
                splited = line.split()
                print(splited)
                try:
                    row.append(classes[int(splited[0])])

                    #print(row)

                    row.append(splited[1])
                    row.append(splited[2])
                    row.append(splited[3])
                    row.append(splited[4])
                    row.append(item[:-4]+".png")
                    row.append(width)
                    row.append(height)
                    final_df.append(row)

                except:
                    pass
    df = pd.DataFrame(final_df)
    df.to_csv(destination_dir+"/saved.csv",index=False)
