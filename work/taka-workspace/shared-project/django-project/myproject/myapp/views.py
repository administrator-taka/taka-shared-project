from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def my_view(request):
    data = request.data
    print(data)

    # Test モデルのすべてのレコードをシリアライザを使ってシリアライズして出力する
    tests = Test.objects.all()
    serializer = TestSerializer(tests, many=True)
    print(serializer.data)

    return Response(serializer.data)

# ここから下は保留
from rest_framework.viewsets import ModelViewSet
from .models import Test
from .serializer import TestSerializer


class TestViewSet(ModelViewSet):
    queryset = Test.objects.all()
    serializer_class = TestSerializer
