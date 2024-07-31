from django import forms
from .models import Topic

class TopicForm(forms.ModelForm):
    # 定义一个字段名映射，将T_name字段映射为"主题名"
    field_classes = {'T_name': 'forms.CharField'}
    
    class Meta:
        model = Topic
        fields = ['T_name']  # 只包含T_name字段
        labels = {'T_name': '主题名'}  # 自定义字段标签
