# python regex pattern example
<br><br>

#### IP
```python
r'^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
```
<br>

#### Domain
```python
r'(([a-zA-Z0-9]+(-[a-zA-Z0-9]+)*\.)+[a-z]{2,10})'
```
<br>

#### Email
```python
r'^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
```
<br>

#### CVE
```python
r'([A-Za-z]){3}[-]([0-9]){4}[-]([0-9]){4,}'
```
<br>

#### Hash
```python
md5_pattern = r"([a-fA-F\d]{32})"
sha1_pattern = r"([a-fA-F\d]{40})"
sha256_pattern = r"([a-fA-F\d]{64})"
```
<br>

<br><br>
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.