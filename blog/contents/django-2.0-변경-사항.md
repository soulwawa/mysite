# Django 2.0 변경 사항
<br><br>
### - Urlpatterns
```python
urlpatterns = [
    # 기존
    url(r'^blog/', include('....')),
    url(r'^(?P<id>\d+)/$', views....),
    # 2.0
    path('blog/', include('...')),
    path('<id>/', views...),
]
```
> 기존 url - > re_path 로 변경

<br>
### - ForeignKey/OneToOneField 필드의 on_delete 인자가 필수로 변경

<br><br>

> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.