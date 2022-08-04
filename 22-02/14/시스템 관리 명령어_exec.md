## exec  
- 주어진 명령어를 실행하는데 새로운 프로세스를 생성하지 않고 쉘 프로세스를 대체함  
예를 들어 bash 쉘에서 자바 프로그램을 실행하면 자바 프로그램의 ppid가 bash 쉘이 되고, 자바 프로그램이 bash 쉘의 하위 프로세스로 실행됨  
exec 커맨드로 실행하면 bash 쉘의 프로세스 자바 프로그램이 됨  
ppid가 따로 없음  
자바프로그램 종료되면 프로세스가 종료됨  
bash 쉘로 돌아오지 않음  
  
## 주요 옵션  
-c : 환경 변수가 없는 상태로 실행  
-a : [name]	0번째 인수로 이름을 전달  
-l : 0번째 인수로 대쉬를 전달  
  
## 사용예제  
```
$ exec echo "aa"
aa

$ exec java -cp '/etc/hadoop/conf' org.apache.hadoop.hdfs.server.datanode.SecureDataNodeStarter
```
  
