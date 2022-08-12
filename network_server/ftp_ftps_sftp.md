## ftp, ftps, sftp(ssh)
- https://nhj12311.tistory.com/76  
- [sshfs 활용해 원격 서버 폴더를 네트워크 드라이브로 연결](https://hbesthee.tistory.com/1567)  


프로토콜: 디바이스 간 데이터 교환하기 위한 통신 규약  
<br>

### ftp
- File Transfer Protocol, 말 그대로 파일 전송하는 통신 규약  
- 기본 포트 21  
- 지금은 보안문제로 잘 사용하지 않음  
<br>

### ftps
- TLS/SSL을 거쳐 안전한 채널  
  - 공개키 암호화 방식 이용해 통신 라인 거쳐 21번, 20번 포트를 안전하게 암호화  
- 결국 서버 공개키로 암호화하면 서버가 가진 비공개 개인키로만 풀 수 있음  
- 공개키가 노출되어도 문제가 없기 때문에 할 수 있는 암호화 방식  
<br>

### SFtp (포트 22)
- ssh의 파일 전송 버전  
- ssh(secure shell)은 telnet의 보안 버전  
- ssh(sftp)에서 터널링 하는 방법은 ftps에서의 방식과 유사  
- **SFtp는 ssh 방식 이용해 안전하게 암호화된 구간에서 ftp 기능 이용 가능**  
<br>
