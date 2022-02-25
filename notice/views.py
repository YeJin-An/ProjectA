from rest_framework.viewsets import ModelViewSet
from notice.models import Notice
from notice.serializers import NoticeSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated

class Notice(ModelViewSet):
  queryset = Notice.objects.all()
  serializer_class = NoticeSerializer


  def get_permaissions(self):
    def get_permissions(self):
      if self.request.method == "GET":
        return [AllowAny()]
      return [IsAuthenticated()]

    def perform_create(self, serializer):
      serializer.save(author=self.request.user)
