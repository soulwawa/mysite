# How to django queryset update() count up down
<br><br>

> django views 에서 단순 숫자 업데이트 방법
```python
from django.db.models import F
post_list.update(views=F('views') + 1)
```

<br><br>

> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.