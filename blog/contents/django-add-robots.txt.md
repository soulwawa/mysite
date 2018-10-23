# Django 2.0 add robots.txt
<br><br>

#### Django 2.0 에 robots.txt 추가 시키는 법 
```python
# myproject/myapp/url.py

from django.views.generic import TemplateView

urlpatterns += [
        path('robots.txt/', TemplateView.as_view(template_name="robots.txt", content_type="text/plain"))
    ]
```

> templates 폴더에 robots.txt 생성

<br><br>

> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.