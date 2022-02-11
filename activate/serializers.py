from rest_framework import serializers
from activate.models import Activate

class ActivateSerializer(serializers.ModelSerializer):
  class Meta:
    model = Activate
    fields = ('id','category','title','content','image','user')