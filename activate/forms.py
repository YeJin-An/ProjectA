from django import forms
from activate.models import Activate

class ActicleForm(forms.ModelForm):
  class Meta:
    model = Activate
    fields = fields = ('id','category','title','content','image','user')