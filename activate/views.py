from rest_framework.viewsets import ModelViewSet
from activate.models import Activate
from activate.serializers import ActivateSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated


# list, detail, create, update, delete를 1개 ViewSet에서 지원

class ActivateViewSet(ModelViewSet):
    queryset = Activate.objects.all()
    serializer_class = ActivateSerializer
    # permission_classes = [IsAuthenticated]

    def get_permissions(self):
        # if self.request.method in ("POST", "PUT", "PATCH", "DELETE"):

        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated()]

    # 유효성 검사가 끝나고 나서
    # 실제 serializer.save()를 할 때 수행되는 함수
    def perform_create(self, serializer):
        # serializer.save는 commit=False를 지원하지 않습니다.
        # 대신 키워드 인자를 통한 속성 지정을 지원합니다.
        serializer.save(author=self.request.user)
