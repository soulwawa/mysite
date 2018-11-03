#### How do i get user ip in django
<br><br>
#### Solved
```python
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
```
<br><br>
> 출처 : stackoverflow
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.