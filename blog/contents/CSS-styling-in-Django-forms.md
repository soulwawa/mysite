#### CSS styling in Django forms
<br><br>
#### Solved #1
```python
class MyForm(forms.Form):
    myfield = forms.CharField(widget=forms.TextInput(attrs={'class' : 'myfieldclass'}))
```

<br>

#### Solved #2
```python
class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel

    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['myfield'].widget.attrs.update({'class' : 'myfieldclass'})
```

<br>

#### Solved #3
```python
class MyForm(forms.ModelForm):
    class Meta:
        model = MyModel
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }
```

<br><br>
> 출처 : stackoverflow
> 본문에 오탈자 및 오류가 있을 경우 피드백 주시면 감사하겠습니다.