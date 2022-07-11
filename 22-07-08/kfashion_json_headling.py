import os, json


# jsonRT, imgRT path
jsonRTPath = "Training/labelData"
imgRTPath = "Training/oriData"

# list dirs in labelData
jsonNameList = os.listdir(jsonRTPath)  
allJsonList = list()

for jsonName in jsonNameList:
    jsonFullPath = os.path.join(jsonRTPath, jsonName)
    allJsonList.append(jsonFullPath)

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

# list for labels
colorList = list()
topSleLengthList = list()
bottomLengthList = list()
opsLengthList = list()
outerLengthList = list()
printPatternList = list()

# json file load
for i, allJson in enumerate(allJsonList[:2000]):
    with open(allJson, 'r') as f:
        jsonData = f.read()
    jsonData = json.loads(jsonData)

    imgName = str(jsonData['이미지 정보']['이미지 식별자']) + '.jpg'
    imgPath = os.path.join(imgRTPath, imgName)

    # for top, outer, ops
    for k, v in jsonData['데이터셋 정보']['데이터셋 상세설명']['라벨링'].items():
        labelDict = v[0]
        if len(labelDict) == 0:
            continue
        
        catRT = jsonData['데이터셋 정보']['데이터셋 상세설명']['라벨링'][k][0]
        if not '카테고리' in catRT:
            continue
        if not '프린트' in catRT:
            continue
        if not '색상' in catRT:
            continue
        if not '소매기장' in catRT:
            continue
        if not '기장' in catRT:
            continue

        color = catRT['색상']
        cat = catRT['카테고리']
        length = catRT['기장']
        sleLength = catRT['소매기장']
        printPattern = catRT['프린트'][0]

        # revise color
        if color == '스카이블루':
            color = '블루'
        if color == '와인':
            color = '레드'
        if color == '카키':
            color = '그린'
        if color == '실버':
            color = '그레이'
        if color == '네이비':
            color = '블루'
        if color == '민트':
            color = '그린'
        if color == '라벤더':
            color = '퍼플'
        if color == '골드':
            color = '옐로우'
        if color == '네온':
            continue

    # for bottom
    for k, v in jsonData['데이터셋 정보']['데이터셋 상세설명']['라벨링'].items():
        labelDict = v[0]
        if len(labelDict) == 0:
            continue
        
        btmcatRT = jsonData['데이터셋 정보']['데이터셋 상세설명']['라벨링'][k]
        if not '카테고리' in catRT:
            continue
        if not '프린트' in catRT:
            continue
        if not '색상' in catRT:
            continue
        if not '기장' in catRT:
            continue

        color = catRT['색상']
        cat = catRT['카테고리']
        length = catRT['기장']
        printPattern = catRT['프린트'][0]

        if color == '스카이블루':
            color = '블루'
        if color == '와인':
            color = '레드'
        if color == '카키':
            color = '그린'
        if color == '실버':
            color = '그레이'
        if color == '네이비':
            color = '블루'
        if color == '민트':
            color = '그린'
        if color == '라벤더':
            color = '퍼플'
        if color == '골드':
            color = '옐로우'
        if color == '네온':
            continue

        # check category_attributes
        if k not in ['상의', '아우터', '하의', '원피스']:
            continue
        if k in ['상의', '아우터', '원피스'] and sleLength == '7부소매':
            sleLength = '긴팔'
        if k == '아우터' and sleLength not in ['긴팔']:
            continue
        if k == '하의' and cat == '청바지':
            cat = "팬츠"
        if k in ['상의', '원피스'] and sleLength not in ['긴팔', '민소매', '반팔']:
            continue          
        if k in ['상의', '아우터'] and length == '노말':
            length = '노멀'
        if k in ['하의', '원피스'] and length == '맥시':
            length = '발목'
        if k == '아우터' and length in ['노멀', '크롭']:
            length = '하프'
        if k == '상의' and length not in ['롱', '크롭']:
            continue
        if k == '아우터' and length not in ['롱', '하프']:
            continue
        if k == '상의' and cat not in ['블라우스', '티셔츠', '셔츠']:
            continue            
        if k == '하의' and cat not in ['팬츠', '스커트']:
            continue            
        if k == '아우터' and cat not in ['재킷', '점퍼', '코트']:
            continue             
        if k == '원피스' and cat not in ['드레스']:
            continue     
        if k in ['상의', '하의', '아우터', '원피스'] and printPattern not in ['무지', '체크', '스트라이프']:
            continue            
        if k in ['하의', '원피스'] and length in ['니렝스', '미디']:
            length = '미니'

        # colorLabel
        if k == '상의' and cat in ['블라우스', '티셔츠', '셔츠']:
            colorLabel = f"{color}_{k}"
            if not colorLabel in colorList:
                colorList.append(colorLabel)
        if k == '하의' and cat in ['팬츠', '스커트']:
            colorLabel = f"{color}_{k}"
            if not colorLabel in colorList:
                colorList.append(colorLabel)
        if k == '아우터' and cat in ['재킷', '점퍼', '코트']:
            colorLabel = f"{color}_{k}"
            if not colorLabel in colorList:
                colorList.append(colorLabel)
        if k == '원피스' and cat in ['드레스']:
            colorLabel = f"{color}_{k}"
            if not colorLabel in colorList:
                colorList.append(colorLabel)

        # topLabel(sleeve)
        if k == '상의' and cat in ['블라우스', '티셔츠', '셔츠']:
            topLabel = f"{sleLength}_{cat}"
            if not topLabel in topSleLengthList:
                topSleLengthList.append(topLabel)
        
        # bottomLabel(length)
        if k == '하의' and cat in ['팬츠', '스커트']:
            bottomLabel = f"{length}_{cat}"
            if not bottomLabel in bottomLengthList:
                bottomLengthList.append(bottomLabel)

        # outerLabel(length)
        if k == '아우터' and cat in ['재킷', '점퍼', '코트']:
            outerLabel = f"{length}_{cat}"
            if not outerLabel in outerLengthList:
                outerLengthList.append(outerLabel)

        # opsLabel(length)
        if k == '원피스' and cat in ['드레스']:
            opsLabel = f"{length}_{cat}"
            if not opsLabel in opsLengthList:
                opsLengthList.append(opsLabel)

        # printPatternLabel(printPattern)
        if k == '상의' and printPattern in ['무지', '체크', '스트라이프']:
            printPatternLabel = f"{printPattern}_{k}"
            if not printPatternLabel in printPatternList:
                printPatternList.append(printPatternLabel)
        if k == '하의' and printPattern in ['무지', '체크', '스트라이프']:
            printPatternLabel = f"{printPattern}_{k}"
            if not printPatternLabel in printPatternList:
                printPatternList.append(printPatternLabel)
        if k == '아우터' and printPattern in ['무지', '체크', '스트라이프']:
            printPatternLabel = f"{printPattern}_{k}"
            if not printPatternLabel in printPatternList:
                printPatternList.append(printPatternLabel)
        if k == '원피스' and printPattern in ['무지', '체크', '스트라이프']:
            printPatternLabel = f"{printPattern}_{k}"
            if not printPatternLabel in printPatternList:
                printPatternList.append(printPatternLabel)

print(len(colorList))
print(len(topSleLengthList))
print(len(bottomLengthList))
print(len(outerLengthList))
print(len(opsLengthList))
print(len(printPatternList))
