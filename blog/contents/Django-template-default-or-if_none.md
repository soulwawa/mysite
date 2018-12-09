#### Django template default or if_none
<br><br>
#### Default Case
> If value evaluates to <b>False</b>
```jinja2
{{ value|default:"nothing" }}
```
<br>

#### If None Case
> If value is <b>None</b>
```jinja2
{{ value|default_if_none:"nothing" }}
```


<br><br>
> 출처 : docs.djangoproject.com
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.