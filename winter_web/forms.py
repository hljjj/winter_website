'''为winter_web创建form.py'''

from django import forms
from .models import Theme,Topic,Entry

class ThemeForm(forms.ModelForm):
    class Meta:
        model=Theme   #根据模型创建一个表单
        fields=['text']     #表单字段为text
        labels={'text':''}  #不要为text生成标签


class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic   #根据模型Topic创建一个表单
        fields=['text']     #表单字段为text
        labels={'text':''}  #不要为text生成标签

class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields=['text']
        labels={'text':''}
        widgets={'text':forms.Textarea(attrs={'cols':80})}
        #widget定制小部件扩宽text输入范围
