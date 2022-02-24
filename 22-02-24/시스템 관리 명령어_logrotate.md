logrotate
===
- 로그 정리할 수 있는 명령어  
- 이 명령어는 데몬이 아니기 때문에 크론탭 이용해 주기적으로 로그 정리하는 명령 추가해야함  
<br>  

## 주요 옵션  
-s : 상태 파일 위치  
-f : 로그 포맷 옵션 지정  
  
## 로그 포맷  
정리할 로그 위치 지정하고 중괄호 이용해 로그 저장  
<br>  
- daily, weekly, monthly, yearly  
  - 일별로 처리  
- rotate  
  - 정리 주기  
- dateext  
  - 일자로 파일 정리  
- compress  
  - 압축  
- rotate  
  - aa  
- notifempty  
  - 파일사이즈가 0이면 처리 안함  
- create  
  - 정리한 로그 파일의 권한 설정  
- copytruncate  
  - 로그를 정리하고 파일 사이즈를 0으로 변경  
- olddir  
  - 정리한 로그를 저장할 위치  
  
