#### Remove all options of select box except 1st option
<br><br>
#### Solved
```javascript
selector.find('option').not(':first').remove();
```


<br><br>
> 출처 : stackoverflow.com
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.