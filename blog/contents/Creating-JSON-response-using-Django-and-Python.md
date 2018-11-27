#### Creating a JSON response using Django and Python
<br><br>
#### Solved - Pre Django 1.7
```python
import json

from django.http import HttpResponse

response_data = {}
response_data['result'] = 'error'
response_data['message'] = 'error message'

return HttpResponse(json.dumps(response_data), content_type="application/json")
```
<br>

#### Solved - Django 1.7 ++
```python
from django.http import JsonResponse
return JsonResponse({'foo':'bar'})
```
<br><br>
> 출처 : stackoverflow.com
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.