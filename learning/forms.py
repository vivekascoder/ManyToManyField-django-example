from django.forms import ModelForm
from .models import Post, Tag
from django.forms.widgets import CheckboxSelectMultiple


class PostCreationForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def __init__(self, *args, **kwargs):
        super(PostCreationForm, self).__init__(*args, **kwargs)
        # Below Two lines are particularly important.
        self.fields['tags'].widget = CheckboxSelectMultiple()
        self.fields['tags'].queryset = Tag.objects.all()
