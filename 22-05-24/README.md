## json.loads()
json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary.  
It is mainly used for deserializing native string, byte, or byte array which consists of JSON data into Python Dictionary.  
<br>
- [[파이썬] json 모듈로 JSON 데이터 다루기](https://www.daleseo.com/python-json/)  

loads() : JSON 문자열을 Python 객체로 변환  
- 일반적으로 파일에 저장되어 있는 JSON 문자열을 읽거나, HTTP 요청의 전문(body)을 읽을 때 자주 사용  

dumps() : Python 객체를 JSON 문자열로 변환  
- indent 파라미터에 숫자를 넘기면 그 만큼 들여쓰기가 되어 JSON 문자열로 변환  
```
json.dumps(json_object, indent=2)
```

load() : JSON 파일을 Python 객체로 불러오기  
- 일반적으로 JSON 포멧의 HTTP 응답 전문(body)을 읽을 때도 이 방식 사용  
```
with open('data.json') as f:
    json_object = json.load(f)
```

dump() : Python 객체를 JSON 파일에 저장  
- Python 객체를 JSON 문자로 변환한 결과를 파일에 바로 쓰고(write) 싶은 경우  
```
with open('data.json', 'w') as f:
    json_string = json.dump(json_object, f, indent=2)
```

<br>

## request.remote_addr
python flask 접속자 IP check  
<br>

## split(separator, maxsplit)
maxsplit = 1이면 최대 1회까지만 문자열 나눔  
maxsplit = 1이면 최대 2회까지,
maxsplit = -1이면 제한없이 문자열 나눔  
