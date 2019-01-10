#### Operation not permitted - /usr/bin/update_rubygems
<br><br>
#### Problem
```text
sudo gem update --system

# Error
Updating rubygems-update
ERROR:  While executing gem ... (Errno::EPERM)
Operation not permitted - /usr/bin/update_rubygems

# Error
ERROR:  While executing gem ... (Gem::FilePermissionError)
You don't have write permissions for the /Library/Ruby/Gems/2.0.0 directory.
```
#### Solved 1
```text
# Install homebrew
http://brew.sh

brew install ruby
```

#### Solved 2
```text
gem install mygem --user-install
```


<br><br>
> 출처 : stackoverflow.com
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.