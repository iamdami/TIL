import os, json, cv2, sys

# jsonRT, imgRT path
jsonRTPath = "Training/labelData"
imgRTPath = "Training/oriData"

# list dirs in labelData
jsonNameList = os.listdir(jsonRTPath)  
allJsonList = [os.path.join(jsonRTPath, jsonName) for jsonName in jsonNameList]

imgNum = 0

for i, allJson in enumerate(allJsonList[:500]):
    
    # dict for column -> num: 82
    labelingDict = {
        "긴팔_블라우스" : 0,
        "민소매_블라우스" : 0,
        "반팔_블라우스" : 0,
        "긴팔_티셔츠" : 0,
        "민소매_티셔츠" : 0,
        "반팔_티셔츠" : 0,
        "긴팔_셔츠" : 0,
        "민소매_셔츠" : 0,
        "반팔_셔츠" : 0,

        "롱_재킷" : 0,
        "하프_재킷" : 0,
        "롱_점퍼" : 0,
        "하프_점퍼" : 0,
        "롱_코트" : 0,
        "하프_코트" : 0,

        "미니_팬츠" : 0,
        "발목_팬츠" : 0,
        "미니_스커트" : 0,
        "발목_스커트" : 0,

        "미니_드레스" : 0,
        "발목_드레스" : 0,

        "상의_화이트" : 0,
        "상의_베이지" : 0,
        "상의_블랙" : 0,
        "상의_그레이" : 0,
        "상의_핑크" : 0,
        "상의_블루" : 0,
        "상의_브라운" : 0,
        "상의_퍼플" : 0,
        "상의_레드" : 0,
        "상의_옐로우" : 0,
        "상의_오렌지" : 0,
        "상의_그린" : 0,
        "아우터_화이트" : 0,
        "아우터_베이지" : 0,
        "아우터_블랙" : 0,
        "아우터_그레이" : 0,
        "아우터_핑크" : 0,
        "아우터_블루" : 0,
        "아우터_브라운" : 0,
        "아우터_퍼플" : 0,
        "아우터_레드" : 0,
        "아우터_옐로우" : 0,
        "아우터_오렌지" : 0,
        "아우터_그린" : 0,
        "하의_화이트" : 0,
        "하의_베이지" : 0,
        "하의_블랙" : 0,
        "하의_그레이" : 0,
        "하의_핑크" : 0,
        "하의_블루" : 0,
        "하의_브라운" : 0,
        "하의_퍼플" : 0,
        "하의_레드" : 0,
        "하의_옐로우" : 0,
        "하의_오렌지" : 0,
        "하의_그린" : 0,
        "원피스_화이트" : 0,
        "원피스_베이지" : 0,
        "원피스_블랙" : 0,
        "원피스_그레이" : 0,
        "원피스_핑크" : 0,
        "원피스_블루" : 0,
        "원피스_브라운" : 0,
        "원피스_퍼플" : 0,
        "원피스_레드" : 0,
        "원피스_옐로우" : 0,
        "원피스_오렌지" : 0,
        "원피스_그린" : 0,

        "상의_무지" : 0,
        "상의_체크" : 0,
        "상의_스트라이프" : 0,
        "하의_무지" : 0,
        "하의_체크" : 0,
        "하의_스트라이프" : 0,
        "아우터_무지" : 0,
        "아우터_체크" : 0,
        "아우터_스트라이프" : 0,
        "원피스_무지" : 0,
        "원피스_체크" : 0,
        "원피스_스트라이프" : 0,
        }

    # json file load
    with open(allJson, 'r') as f:
        jsonData = f.read()
    jsonData = json.loads(jsonData)

    imgName = str(jsonData['이미지 정보']['이미지 식별자']) + '.jpg'
    txtName = str(jsonData['이미지 정보']['이미지 식별자']) + '.txt'
    imgPath = os.path.join(imgRTPath, imgName)

    # dict for append labels
    tmplabeldict = dict()
    jsonDataDict = jsonData['데이터셋 정보']['데이터셋 상세설명']['라벨링']
    del jsonDataDict['스타일']

    for k, v in jsonDataDict.items():
        tmplabeldict[k] = list()  # list of keys
        if len(v[0].keys()) > 0:  # if k has key
            for value_k, value_v in v[0].items():
                if value_k in ['디테일', '소재', '넥라인', '핏']:
                    continue
                if isinstance(value_v, list):
                    value_v = value_v[0]

                # revise color
                if value_v in ['스카이블루', '네이비']:
                    value_v = '블루'
                if value_v == '골드':
                    value_v = '옐로우'
                if value_v == '와인':
                    value_v = '레드'
                if value_v == '카키':
                    value_v = '브라운'
                if value_v == '실버':
                    value_v = '그레이'
                if value_v == '민트':
                    value_v = '그린'
                if value_v == '라벤더':
                    value_v = '퍼플'

                # check category_attributes
                if value_v == '7부소매':
                    value_v = '긴팔'
                if value_v in ['노멀', '노말', '크롭']:
                    value_v = '하프'
                if value_v in ['니렝스', '미디']:
                    value_v = '미니'
                if value_v == '맥시':
                    value_v = '발목'
                if value_v == '청바지':
                    value_v = '팬츠'
                if value_v == '탑':
                    value_v = '티셔츠'

                tmplabeldict[k].append(value_v)

    for k, v in tmplabeldict.items():
        if len(v) > 0:  # if k has value
            for value_v in v:
                if '무지' in v:
                    label = f'{k}_{value_v}'
                    if label in labelingDict.keys():
                        labelingDict[label] += 1  # cnt
                        
            for labeling_k in labelingDict.keys():
                labelingList = labeling_k.split('_')
                if labelingList[0] in v and labelingList[1] in v:
                    labelingDict[labeling_k] += 1 

# ---------- have no idea.-----------
    kCnt = 0
    for k, v in labelingDict.items():
        if v == 1:
            kCnt += 1

    if imgNum < 50:
        if kCnt >= 5:
            appendList = list()
            for k, v in labelingDict.items():
                appendList.append(v)
            appendList.insert(0, imgName)
            appendList = list(map(str, appendList))
            txt = ' '.join(appendList)

            with open(f"appendListTxt.txt", "a") as f:
                f.write(f"{txt}\n")
            
            imgNum += 1
        sys.exit()

            
