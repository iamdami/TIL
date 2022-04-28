## service
- [서비스 목록 확인과 서비스 명령어들, reload와 restart의 차이점](https://fabxoe.tistory.com/130)  
- [서비스 등록, 관리](https://victorydntmd.tistory.com/215)  
<br>

## systemd 에서 service 관리  
**<서비스 상태표시>**  
- 존재하는 전체 서비스 목록: systemctl 
- 서비스 목록 (활성화 여부만 표시): systemctl list-unit-files  
- 부팅시 실행에 실패한 서비스목록: systemctl --failed  
- 서비스 활성화 여부: systemctl is-enabled [서비스명]  
- 서비스 현재 동작 여부: systemctl is-active [서비스명]  
- 서비스의 자세한 상태 (해당 서비스의 로그도 표시): systemctl status -l [서비스명]  
<br>

**<서비스 제어>**  
서비스 활성화하면 부팅시 해당 서비스 자동실행  
- 서비스 활성화: systemctl enable [서비스명]  
- 서비스 비활성화: systemctl disable [서비스명]  
- 서비스 시작: systemctl start [서비스명]  
- 서비스 종료: systemctl stop [서비스명]  
- 서비스 재시작: systemctl restart [서비스명]  
- 서비스 갱신: systemctl reload [서비스명]  
<br>

서비스 설정 즉시 반영하려면  
systemctl daemon-reload  
<br>

- 서비스와 관련된 프로세스도 모두 죽임: systemctl kill [서비스명]  
<br>

## 로그 파일 확인
대부분의 시스템 로그 파일들은 /var/log에 있음  
/var/log 디렉토리 이동 후 ls -l 명령어로 시스템 로그 파일들 확인 가능  
<br>

- syslog  
  - 제일 중심적인 로깅 시스템  
  - kernel, application 등과 관련된 메시지들을 확인 가능  
  - 조금 더 확장하면 데이터 센터의 모든 로그 파일들 저장 가능  
- auth.log  
  - 인증(authentication)의 실패와 성공 기록이 담겨있음  
- messages  
  - 모든 종류의 일반적인 시스템 메시지가 담겨있음  
<br>

**<파일 확인에 유용한 명령어>**  
- cat  
- less  
  - pagination과 scroll을 통해 파일을 보여줌  
- grep  
  - 파일 안에 특정 문자열을 찾고 싶을 때 사용  
  - grep PATTERN [FILE] 과 같이 사용  
- head  
  - 파일의 첫 줄 보여줌  
- tail  
  - 파일의 마지막 줄 보여줌  
  - 주로 로그 파일 확인할 때 tail -f /var/log/syslog 와 같이 사용  
