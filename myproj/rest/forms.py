from datetime import datetime
from django.core.exceptions import ValidationError
from django import forms
#from django.utils.translation import ugettext_lazy as _


class PostForm(forms.Form):
    title = forms.CharField(help_text="제목을 입력하세요")
    content = forms.CharField(help_text="내용을 입력해 주세요")
    created_at = forms.DateField()
    updated_at = forms.DateField()

    def check_updated(self):
        # 값을 가져온다.
        data = self.cleaned_data["updated_at"]
        if data < datetime.date.today():
            raise ValidationError("오늘 보다 이전 시간 입력")
        return data
