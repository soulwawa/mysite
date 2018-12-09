#### Django admin pagination
<br><br>
#### Solved
```python
class UserAdmin(admin.ModelAdmin):
    model = User
    list_per_page = 5 # pagination
```

<br><br>
> 출처 : stackoverflow.com
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.