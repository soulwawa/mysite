# Django orm order_by capitalize-alphabet
<br><br>

#### ORM 정렬할때 대문자 소문자 상관없이 정렬 하고 싶은경우
```python
from django.db.models.functions import Lower
MyModel.objects.order_by(Lower('myfield'))
```

<br><br>
> 출처 : stackoverflow

> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.