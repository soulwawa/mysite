#### How do downgrade node or install a specific previous version
<br><br>
#### Solved

```commandline
brew search node

# install the desired version
brew install node@8

brew install unlink node

brew install node@8

brewlink node@8
```

#### Another Solved 
```commandline
brew link --force --overwrite node@8
```
<br><br>
> 출처 : apple.stackexchange.com
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.