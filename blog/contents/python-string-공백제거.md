# Neo4j Cypher Query
<br><br>
### 사이퍼의 핵심 단어들
#### MATCH
> 데이터베이스가 일치해야 하는 패턴을 설명, 쿼리를 시작하는 구조적 구성 요소며, 가장 중요한 부분이다. ( = SELECT )
```sql
MATCH (me:Person)  - [:KNOWS] - (friend)
```

#### WHERE
> 특정 기준에 일치하는 항목을 필터링
```sql
WHERE me.name = 'my name' AND me.age > 18
```

#### RETURN
> 결과를 반환한다.
> 경로, 노드, 관계, 해당 속성 또는 언급된 매개변수 집합을 반환
> 모든 읽기 쿼리, 일부 쓰기 쿼리가 데이터를 반환
```sql
RETURN me.name, collect(friend), count(*) as friends
```

#### WITH
> 하나의 쿼리 파트에서 다음 쿼리 파트로 결과를 전달한다.
> 결과가 집합에 데이터를 포함하는 대신, 조희의 다음 부분으로 전달된다.
> 결과를 전달하고 집계하며 READ 및 UPDATE 문도 분리한다.

#### ORDER BY SKIP LIMIT
> 결과를 정렬하고 페이지화

#### CREATE
> 해당 속성을 가진 노드와 관계를 작성
> CREATE UNIQUE - 중복되지 않는 노드와 관계만 생성
```sql
CREATE (p:Person), (p) - [:KNOWS {sincd:2010}] -> (me:Person {name:"My Name"})
```

#### MERGE
> 패턴의 일부가 이미 있는경우는 MATCH, 패턴이 아직 존재하지 안흔 경우에는 CREATE 연산을 수행
> 인덱스와 잠금을 사용한다.
```sql
MERGE (me:Person {name:"MY NAME"}) ON
MATCH me
SET me.accessed = timestamp()
ON CREATE me
SET me.age =42
```

#### SET, REMOVE
> 노드 및 / 또는 관계에 대한 속성과 레이블을 업데이트 한다.
```sql
SET me.age =42
SET me:Employee
REMOVE me.first_name
REMOVE me:Contractor
```

### DELETE
> 노드와 관계를 삭제한다.
```sql
MATCH (me) OPTIONAL MATCH (me)-[r]-()
DELETE me, r
```

<br><br>

> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.