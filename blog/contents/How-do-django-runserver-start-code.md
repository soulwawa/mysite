#### How do django runserver start code
<br><br>
#### Solved
```python
# blog/apps.py
from django.apps import AppConfig


class BlogConfig(AppConfig):
    name = 'blog'

    def ready(self):
        # TODO : Write your codes to run on start up
        pass

```
<br><br>
> 출처 : https://docs.djangoproject.com/en/2.1/ref/applications/
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.