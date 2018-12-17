#### python how to full traceback with try catch
<br><br>
#### Solved
```python
import traceback

try:
    do_something()
except Exception:
    print(traceback.format_exc())
    # or
    traceback.print_exc()
```

<br><br>
> 출처 : 
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.