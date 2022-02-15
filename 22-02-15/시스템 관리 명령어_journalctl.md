## journalctl  
- ```systemctl```로 실행한 ```systemd``` 로그를 확인할 수 있는 명령어  

## 주요 옵션
-u : 로그 출력할 유닛 지정  
-o : 출력 형식 지정 (short, short-iso)  
-f : 신규로 추가 되는 로그 출력  
  
## 출력 형식  
short : 기본값. 한 행에 하나의 Log만 출력  
short-iso : 기본값에 ISO 8601의 시간 형식으로 출력  
short-precise : 기본값에 마이크로 초 단위로 시간 출력  
short-monotonic : 기본값에 단조로운 시간 형식으로 출력  
verbose : 전체 Log를 모두 자세하게 출력  
json : json 형식  
json-pretty : json 형식을 보기 편하게 출력  
json-see : json 형식을 Server-Sent Events에 적합한 형식으로 출력  
cat : 간결하게 출력  
