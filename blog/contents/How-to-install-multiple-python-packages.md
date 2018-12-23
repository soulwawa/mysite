#### How to install multiple python packages
<br><br>
#### Solved
```text
pip install django, redis, django-redis # not working
```
 
```text
# make requirements.txt

django==2.1.2
django-redis==4.10.0
```

```text
pip install -r requirements.txt
```

<br><br>
> 출처 : 
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.