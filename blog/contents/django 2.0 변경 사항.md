# Django 2.0 변경 사항

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

### - ForeignKey/OneToOneField 필드의 on_delete 인자가 필수로 변경


