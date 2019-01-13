#### Can I query MongoDB ObejctId by date
<br><br>
#### Solved python, pymongo
```python
import datetime
from bson.objectid import ObjectId
mins = 15
gen_time = datetime.datetime.today() - datetime.timedelta(mins=mins) 
dummy_id = ObjectId.from_datetime(gen_time)
result = list(db.coll.find({"_id": {"$gte": dummy_id}}))

```

<br><br>
> 출처 : stackoverflow.com
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.