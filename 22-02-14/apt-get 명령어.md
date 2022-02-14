## 패키지 설치  
패키지간 의존성 확인해 자동으로 설치해 주기 때문에 사용 편리  
- yum  
  - 레드햇 계열  
  - CentOS  
  
- **apt-get**  
  - 데비안 계열  
  - 우분투  

## Ubuntu apt-get 명령어 정리
우분투에는 GUI로 되어있는 관리자도 있긴 하지만 CUI인 apt-get이 편함  
- 패키지 인덱스 정보 업데이트  
  - apt-get은 인덱스 가지고 있는데, 이 인덱스는 /etc/apt/sources.list 에 있음  
    이곳에 저장된 저장소에서 사용할 패키지 정보 얻음  
```sudo apt-get update```  
  
- 설치된 패키지 업그레이드  
  - 설치되어 있는 패키지를 모두 새 버전으로 업그레이드  
```sudo apt-get upgrade```  
  - 의존성 검사하며 설치  
```sudo apt-get dist-upgrade```
  
- 패키지 설치  
```sudo apt-get install 패키지이름```  

- 패키지 재설치  
```apt-get --reinstall install 패키지이름```  
  
- 패키지 삭제  
  - 설정 파일은 지우지 않음  
```sudo apt-get remove 패키지이름```  
  - 설정 파일까지 모두 지움  
```sudo apt-get --purge remove 패키지이름```  
  
- 패키지 소스코드 다운로드  
```sudo apt-get source 패키지이름```  
  - 위에서 받은 소스코드를 의존성있게 빌드  
```sudo apt-get build-dep 패키지이름```  
  
- 패키지 검색  
```sudo apt-cache  search 패키지이름```  
  
- 패키지 정보 보기  
```sudo apt-cache show 패키지이름```  
<br>
apt를 이용해 설치된 deb 패키지는 /var/cache/apt/archive/ 에 설치됨  

## rpm, deb 파일  
두 파일은 모두 응용프로그램 설치 파일  
- 패키지 파일  
  - rpm: 레드햇 계열  
  - deb: 데비안 계열  
  
패키지를 설치시 파일 이용할 수도 있지만, apt-get 명령어 이용하면 의존성 자동으로 관리해줘 편리함  
