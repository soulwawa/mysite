#### dev/sd1 contains a file system with errors
<br><br>
#### Problem
```text
/dev/sda1 contains a file system with errors, check forced.
Inodes that were part of a corrupted orphan linked list found.
/dev/sda1: UNEXPECTED INCONSISTENCY: RUN fsck MANUALLY.
         (i.e., without -a or -p options)
fsck exited with status code 4
The root filesystem on /dev/sda1 requires a manual fsck
BusyBox v1.22.1 (Ubuntu 1:1.22.0-19ubuntuu2) built-in shell (ash)
Enter 'help' for a list of built-in commands.
(initramfs)_

```


#### Solved
```text
fsck -f /dev/sda1
```

<br><br>
> 출처 : askubuntu.com
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.