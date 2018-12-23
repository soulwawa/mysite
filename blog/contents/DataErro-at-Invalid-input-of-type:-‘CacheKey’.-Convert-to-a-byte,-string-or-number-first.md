#### DataError at Invalid input of type: ‘CacheKey’. Convert to a byte, string or number first.
<br><br>
#### Solved
```text
# Your pip check

pip list
pip install redis --upgrade

# django used..
pip install django-redis --upgrade
pip install django-redis-cache --upgrade
```

<br><br>
> 출처 : stackoverflow.com
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.