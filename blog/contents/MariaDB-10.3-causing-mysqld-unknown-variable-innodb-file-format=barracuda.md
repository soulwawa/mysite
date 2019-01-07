#### MariaDB 10.3 causing mysqld: unknown variable 'innodb-file-format=barracuda’
<br><br>
#### Solved
- innodb_file_format Default Value: Barracuda (>= MariaDB 10.2.2) Antelope (<= MariaDB 10.2.1) Deprecated: MariaDB 10.2, Removed: MariaDB 10.3.1
This means this must be removed and is on by default.

- innodb_file_per_table Default Value: ON (>= MariaDB 5.5), OFF (<= MariaDB 5.3)
This means it should be removed because it is on by default.

- innodb_large_prefix Default Value: ON (>= MariaDB 10.2.2) OFF (<= MariaDB 10.2.1) Deprecated: MariaDB 10.2 Removed: MariaDB 10.3.1

<br><br>
> 출처 : https://github.com/frappe/bench/issues/681
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.