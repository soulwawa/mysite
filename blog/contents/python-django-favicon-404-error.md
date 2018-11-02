#### python django favicon 404 error
<br><br>
#### bash.html ADD
```djangotemplate
<link rel="icon" href="{% static 'img/favicon.ico' %}">
```

#### urls.py ADD
```python
from django.urls import path
from django.contrib.staticfiles.storage import staticfiles_storage
from django.views.generic.base import RedirectView

# favicon
path('favicon.ico/', RedirectView.as_view(url=staticfiles_storage.url('image/favicon.png'))),
```

<br><br>
> 출처 : http://www.tumblingprogrammer.com
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.