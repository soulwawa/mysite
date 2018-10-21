# Django logging.handlers
<br><br>

#### StreamHandler
> (stream=None) sys.stdout, sys.stderr 등의 파일객체로의 출력

#### FileHandler
> (filename, mode='a', encoding=None, delay=False) : 디스크 파일로의 출력.

#### NullHandler : 어떠한 포맷팅/출력도 수행하지 않습니다. <br>

#### RotatingFileHandler
> (filename, mode='a', maxBytes=0, backupCount=0, encoding=None, delay=False)
> maxBytes 단위로 로그 파일을 생성하되, 최대 backupCount 개수만큼만 유지

#### TimedRotatingFileHandler
> (filename, when='h', interval=1, backupCount=0, encoding=None, delay=False, utc=False, atTime=None)
> 지정 시간 단위로 로그 파일을 생성하되, 최대 backupCount 개수만큼만 유지

#### SocketHandler (host, port)
> 지정 서버/포트로의 TCP 출력

#### DatagramHandler (host, port) 
> UDP 소켓

#### SysLogHandler (address=('localhost', SYSLOG_UDP_PORT), facility=LOG_USER, socktype=socket.SOCK_DGGRAM)
> 유닉스의 로그 인터페이스인 syslog 서버로의 출력

#### SMTPHandler (mailhost, fromaddr, toaddrs, subject, credentials=None, secure=None, timeout=1.0)
> SMTP 프로토콜을 활용하여 이메일 발송

#### HTTPHandler (host, url, method='GET', secure=False, credentials=None, context=None)
> GET 혹은 POST 방식으로 출력

<br><br>
> 출처 : Ask Company

> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.