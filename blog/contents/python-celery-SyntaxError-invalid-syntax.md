# python celery SyntaxError: invalid syntax
<br><br>

> python celery SyntaxError: invalid syntax
~~~python

File "/home/george/projects/.virtualenvs/nswa/lib/python3.7/site-packages/celery/backends/redis.py", line 22
    from . import async, base
                      ^
SyntaxError: invalid syntax

~~~
> python 3.7 에서 지원이 안되는 문제
> celery 4.2 do not support python 3.7
> async와 await 는 이제 예약 키워드입니다.

<br><br>

> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.