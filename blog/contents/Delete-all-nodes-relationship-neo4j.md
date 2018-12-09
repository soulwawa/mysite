#### Delete all nodes relationship neo4j
<br><br>
#### Solved Neo4j: 2.3.0 ~ 3.3.0
```text
MATCH (n)
DETACH DELETE n
```
<br>

#### Solved Neo4j: ~ 2.3.0
```text
MATCH (n)
OPTIONAL MATCH (n)-[r]-()
DELETE n,r
```
<br><br>
> 출처 : stackoverflow.com
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.