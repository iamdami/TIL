import os, json,cv2
# jsonRT, imgRT path
jsonRTPath = "Training/labelData"
imgRTPath = "Training/oriData"
# list dirs in labelData
jsonNameList = os.listdir(jsonRTPath)  
allJsonList = [os.path.join(jsonRTPath, jsonName) for jsonName in jsonNameList]
# dict for column -> num: 81

# json file load
for i, allJson in enumerate(allJsonList[100:120]):
    # dict for column -> num: 81
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
    with open(allJson, 'r') as f:
        jsonData = f.read()
    jsonData = json.loads(jsonData)
    imgName = str(jsonData['이미지 정보']['이미지 식별자']) + '.jpg'
    imgPath = os.path.join(imgRTPath, imgName)
    tmplabeldict = dict()
    for k, v in jsonData['데이터셋 정보']['데이터셋 상세설명']['라벨링'].items():
        if k != '스타일':
            tmplabeldict[k] = list()
            if len(v[0].keys()) > 0:
                for kk,vv in v[0].items():
                    if isinstance(vv,list):
                        vv = vv[0]
                    if vv == '7부소매':
                        vv = '긴팔'
                    tmplabeldict[k].append(vv)
    print('='*20)
    cv2.imwrite(f"tmpimg/{imgName}",cv2.imread(imgPath))
    print(imgName)
    for k,v in tmplabeldict.items():
        if len(v)>0:
            for vv in v:
                if '무지' in v:
                    label = f'{k}_{vv}'
                    if label in labelingDict.keys():
                        labelingDict[label] += 1
            for tmpkey in labelingDict.keys():
                labelList = tmpkey.split('_')
                if labelList[0] in v and labelList[1] in v:
                    labelingDict[tmpkey] += 1
    for k,v in labelingDict.items():
        if v > 0:
            print(k,v)
    print('='*20)
