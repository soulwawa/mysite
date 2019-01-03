#### Javascript MAX MIN
<br><br>
#### Solved

```javascript
var temp = [0, 7, 3, 1, 9, 8, 5];

Math.max.apply(null, temp); //결과값은 9
Math.min.apply(null, temp); //결과값은 0
```

#### RangeError: Maximum call stack size exceeded Case
```javascript
var temp = [0, 7, 3, 1, 9, 8, 5];

var max = temp.reduce( function (a, b) { 
    return a > b ? a:b;
});

var min = temp.reduce( function (a, b) { 
    return a > b ? b:a;
});
```
<br><br>
> 출처 : 
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.