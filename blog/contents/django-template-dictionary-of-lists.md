#### django template and dictionary of lists
<br><br>
#### Solved
```djangotemplate
{% for key, value_list  in example_dictionary.items %}
  {{key}}
  {% for value in value_list %}
   {{value}}
  {% endfor %}
{% endfor %}
```
a
<br><br>
> 출처 : 
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.