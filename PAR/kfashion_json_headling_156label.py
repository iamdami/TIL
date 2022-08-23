import os, json, cv2

# jsonRT, imgRT path
jsonRTPath = "Training/labelData"
imgRTPath = "Training/oriData"

# list dirs in labelData
jsonNameList = os.listdir(jsonRTPath)  
jsonPathList = [os.path.join(jsonRTPath, jsonName) for jsonName in jsonNameList]

keyList = list()
delKeyList = ["디테일", "소재", "핏", "서브색상", "옷깃", "넥라인"]

# 119
labelingKeyList = ['하의_발목', '하의_블랙', '하의_팬츠', '하의_무지', '하의_미니', '하의_화이트', '상의_노멀', '상의_스카이블루', '상의_블라우스', '상의_무늬', '하의_미디', '하의_스커트', '하의_청바지', '아우터_하프', '아우터_베이지', '아우터_재킷', '아우터_체크', '하의_그레이', '상의_블루', '상의_후드티', '상의_긴팔', '상의_무지', '상의_롱', '상의_브라운', '상의_티셔츠', '원피스_브라운', '원피스_드레스', '원피스_긴팔', '원피스_무지', '아우터_그린', '아우터_반팔', '상의_그린', '상의_셔츠', '상의_반팔', '상의_하프' '아우터_카키', '아우터_가디건', '아우터_긴팔', '아우터_노멀', '아우터_무지', '상의_블랙', '하의_블루', '하의_무늬', '상의_화이트', '상의_니트웨어', '아우터_코트', '아우터_오렌지', '상의_퍼플', '하의_네이비', '상의_베이지', '하의_핑크', '상의_탑', '하의_베이지', '상의_핑크', '하의_민트', '원피스_미디', '원피스_스카이블루', '하의_스카이블루', '상의_민소매', '아우터_그레이', '아우터_베스트', '아우터_민소매', '아우터_퍼플', '원피스_블랙', '상의_그레이', '원피스_민소매', '아우터_블랙', '상의_카키', '아우터_스트라이프', '하의_레드', '상의_레드', '상의_오렌지', '상의_스트라이프', '아우터_롱', '아우터_네이비', '아우터_무늬', '아우터_블루', '원피스_화이트', '원피스_반팔', '원피스_무늬', '하의_카키', '원피스_베이지', '아우터_점퍼', '아우터_패딩', '상의_네이비', '원피스_퍼플', '아우터_핑크', '하의_래깅스', '원피스_미니', '원피스_레드', '하의_그린', '아우터_화이트', '상의_민트', '상의_체크', '하의_오렌지', '상의_옐로우', '원피스_그린', '원피스_체크', '원피스_발목', '원피스_스트라이프', '원피스_핑크', '아우터_짚업', '원피스_그레이', '원피스_옐로우', '아우터_브라운', '원피스_점프수트', '원피스_네이비', '하의_체크', '아우터_스카이블루', '원피스_오렌지', '하의_브라운', '아우터_레드', '하의_스트라이프', '원피스_블루', '하의_옐로우', '원피스_민트', '원피스_카키', '아우터_민트', '하의_퍼플', '아우터_옐로우']

print(len(labelingKeyList))
img_cnt = 0

for i, jsonPath in enumerate(jsonPathList[:51000]):
    labelingDict = dict()
    # labeling num : 156
    for finalKey in labelingKeyList:
        labelingDict[finalKey] = 0

    with open(jsonPath, "r") as jsonFile:
        jsonData = jsonFile.read()
    jsonData = json.loads(jsonData)

    oneImgName = str(jsonData["이미지 정보"]["이미지 식별자"]) + ".jpg"
    oneImgPath = os.path.join(imgRTPath, oneImgName)

    # dict for  set location sth
    jsonDataDict = jsonData["데이터셋 정보"]["데이터셋 상세설명"]["라벨링"]
    del jsonDataDict["스타일"]

    for k, v in jsonDataDict.items():
        v = v[0]
        for delKey in delKeyList:
            if delKey in v:
                del v[delKey]

        if "프린트" in v:
            v["프린트"] = v["프린트"][0]        
            if  v["프린트"] not in ["무지", "체크", "스트라이프"]:
                v["프린트"] = "무늬"

        for kk, vv in v.items():
            appendKey = f"{k}_{vv}"
            if appendKey in labelingDict:
                labelingDict[appendKey] += 1

    print(oneImgName)

    ################################################################################

    num_cnt = 0
    for k, v in labelingDict.items():
        if v == 1:
            num_cnt += 1
    
    if img_cnt < 38500:
        if num_cnt >= 4:
            appendList = list()
            for kk, vv in labelingDict.items():
                appendList.append(vv)
            appendList.insert(0, f"{oneImgPath}")
            appendList = list(map(str, appendList))
            write_txt = " ".join(appendList)

            cv2.imwrite(f"KFdataset/trainImg/{oneImgName}", cv2.imread(oneImgPath))
            with open(f"for_train.txt", "a") as txtFile:
                txtFile.write(f"{write_txt}\n")
            img_cnt += 1

    elif img_cnt >= 38500 and img_cnt < 47500:
        if num_cnt >= 4:
            appendList = list()
            for kk, vv in labelingDict.items():
                appendList.append(vv)
            appendList.insert(0, f"{oneImgPath}")
            appendList = list(map(str, appendList))
            write_txt = " ".join(appendList)

            cv2.imwrite(f"KFdataset/testImg/{oneImgName}", cv2.imread(oneImgPath))
            with open(f"for_test.txt", "a") as txtFile:
                txtFile.write(f"{write_txt}\n")
            img_cnt += 1

    elif img_cnt >= 47500:
        exit()
