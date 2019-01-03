#### ChartJS Formatting Y axis
<br><br>
#### Solved
```javascript
var options = {
    scales: {
        yAxes: [
            {
                ticks: {
                    callback: function(label, index, labels) {
                        return label/1000+'k';
                    }
                },
                scaleLabel: {
                    display: true,
                    labelString: '1k = 1000'
                }
            }
        ]
    }
}
```


<br><br>
> 출처 : stackoverflow.com
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.