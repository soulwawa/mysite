#### How To Change Input Placeholder Color
<br><br>
#### Solved
```html
<input type="text" placeholder="input text...">
```
```css
::placeholder {    /* Chrome, Firefox, Opera, Safari 10.1+ */
    color: red;
   opacity: 1; /* Firefox */
}

:-ms-input-placeholder { /* Internet    Explorer 10-11 */
    color: red;
}

::-ms-input-placeholder    { /* Microsoft Edge */
    color: red;
}
```

<br><br>
> 출처 : w3schools.com
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.