from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def my_view(request):
    data = request.data
    print(data)
    # データベースから値を取得する処理を実装する
    return Response("Response from API")


from rest_framework.viewsets import ModelViewSet
from .models import Test
from .serializer import TestSerializer


class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
