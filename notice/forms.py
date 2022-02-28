from django import forms
from notice.models import Notice

class NoticeForm(forms.ModelForm):
  class Meta:
    model = Notice
    fields = "__all__"

  def clen_title(self):
    title = self.cleaned_data.get("title")
    if title:
      if ((len(title)<5)and(len(title)!=5)):
        raise forms.ValidationError("5글자만!!") 
    return title
