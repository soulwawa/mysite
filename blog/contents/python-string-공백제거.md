# Python String 공백제거
<br><br>
### 1. 양쪽 끝의 공백 문자를 제거하는 방법
~~~python

temp = ' hallo 3es '
temp.strip()  # 'hallo 3es'

~~~

### 2. 모든 공백 제거하는 방법
~~~python

# ex1)
temp = ' hallo 3es'
temp.replace(' ', '')  # 'hallo3es'

# ex2)
import re
temp = ' hallo 3es'
pattern = re.compile(r'\s+')
result = re.sub(pattern, '', temp)  # 'hallo3es'

# ex3)
''.join(temp.split())  # 'hallo3es'

~~~
<br><br>

> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.