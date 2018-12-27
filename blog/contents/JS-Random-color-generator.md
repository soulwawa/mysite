#### JS Random color generator
<br><br>
#### Solved #1
```javascript
"#"+((1<<24)*Math.random()|0).toString(16)
```

#### Solved #2
```javascript
'#'+Math.random().toString(16).substr(-6);  // three-numbers format

'#'+Math.random().toString(16).slice(-3)  // six-numbers format
```

#### Solved #3
```javascript
'#' + (Math.random().toString(16) + "000000").substring(2,8)
```

#### Solved #4
```javascript
'#'+Math.floor(Math.random()*16777215).toString(16);
```

<br><br>
> 출처 : 
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.