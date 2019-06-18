from django.forms import ModelForm, Textarea
from .models import *
from django.contrib.auth.models import User


class writeblog(ModelForm):
    class Meta:
        model = Post
        fields = ('title','content','slug')


    def save(self, user_id ,commit=True,):
        form=super(writeblog, self).save(commit=False)
        form.author=User.objects.get(pk=user_id)
        if commit:
            form.save()
            return form
