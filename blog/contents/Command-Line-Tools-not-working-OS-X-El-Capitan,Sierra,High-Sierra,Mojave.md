#### Command Line Tools not working - OS X El Capitan, Sierra, High Sierra, Mojave
<br><br>
#### Error Message
```commandline
crun: error: invalid active developer path
 (/Library/Developer/CommandLineTools), missing xcrun at:
 /Library/Developer/CommandLineTools/usr/bin/xcrun
```

#### Solved
```commandline
xcode-select --install
```

<br><br>
> 출처 : stackoverflow
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.