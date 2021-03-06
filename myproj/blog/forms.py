import os
from django import forms
from .models import Blog, Comment


class BlogForm(forms.ModelForm):
    def clean_file(self):
        file = self.cleaned_data.get('file', None)
        if file:
            extension = os.path.splitext(file.name)[-1].lower()
            if extension not in ('.mp4', '.avi'):
                raise forms.ValidationError('비디오 파일을 업로드해주세요.')
        return file

    class Meta:
        model = Blog
        fields = ['title',
                  'description',
                  'start_dt', 'end_dt'
                  'file',
                  'photo']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = [
            'content',
        ]
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3}),
        }
