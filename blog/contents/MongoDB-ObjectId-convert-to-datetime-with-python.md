#### MongoDB ObjectId convert to datetime with python
<br><br>
#### python package pymongo
```python
import datetime
from bson.objectid import ObjectId
mins = 15
gen_time = datetime.datetime.today() - datetime.timedelta(mins=mins) 
dummy_id = ObjectId.from_datetime(gen_time)
result = list(db.coll.find({"_id": {"$gte": dummy_id}}
```

#### 60일 이전 데이터 쿼리
```python
db.collection.find({_id: {$lt:new ObjectId( Math.floor(new Date(new Date()-1000*60*60*24*60).getTime()/1000).toString(16) + "0000000000000000" )}})
```

#### 시간순 정렬
```python
items = db.your_collection.find().sort("_id", pymongo.ASCENDING)
items = db.your_collection.find().sort("_id", pymongo.DESCENDING)


```
<br><br>
> 출처 : https://code.i-harness.com
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.