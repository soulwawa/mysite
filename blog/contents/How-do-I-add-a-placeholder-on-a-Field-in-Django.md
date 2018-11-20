#### How do I add a placeholder on a Field in Django?
<br><br>
#### Solved #1
```python
class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Name'}),
            'description': forms.Textarea(
                attrs={'placeholder': 'Enter description here'}),
        }
```
<br>

#### Solved #2
```python        
q = forms.CharField(label='search', 
                    widget=forms.TextInput(attrs={'placeholder': 'Search'}))
```

<br><br>
> 출처 : stackoverflow.com
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.