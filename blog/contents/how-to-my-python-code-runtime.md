# how to my python code runtime
<br><br>

#### Python Code 실행 시간 체크하는 방법
```python
# terminal, bash, zsh

def function_to_test(n):
    for i in range(n):
        pass

import timeit
start = timeit.default_timer()

# 여기에 측정할 코드를 넣으세요
function_to_test(300000)


stop = timeit.default_timer()
print(stop - start)

```

<br><br>
> 출처 : Hashcode.co.kr
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.