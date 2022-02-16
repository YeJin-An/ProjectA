from django import forms
from activate.models import Activate

class ActicleForm(forms.ModelForm):
  class Meta:
    model = Activate
    fields = fields = ('id','category','title','content','image','user')

    def clean_title(self):
        title = self.cleaned_data.get("title")
        if title:
            if len(title) < 3:
                raise forms.ValidationError("3글자 이상!!")
        return title