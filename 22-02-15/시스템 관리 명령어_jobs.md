## jobs
- 현재 계정에서 실행중인 작업 표시  

## 주요 옵션  
-l : 프로세스 ID 표시  

## 사용예제  
### 프로세스 상태  
Running : 실행 중  
Stopped : 일시 중단(Ctrl + Z 입력)  
Terminated : 강제 종료(kill 명령 종료)  
Done : 정상 종료  
  
```
# 실행중인 프로세스를 표시 
$ jobs 
[1]   Stopped                 watch date
[2]   Stopped                 watch date
[3]   Stopped                 watch date
[4]-  Stopped                 watch date
[5]+  Stopped                 watch date

# 실행 중인 프로세스의 PID 확인 
$ jobs -l
[1]  18129 Stopped                 watch date
[2]  18188 Stopped                 watch date
[3]  19726 Stopped                 watch date
[4]- 19741 Stopped                 watch date
[5]+ 19751 Stopped                 watch date
```
  
[] : 작업 순서  
- : 이전 프로세스, + : 현재 프로세스  
