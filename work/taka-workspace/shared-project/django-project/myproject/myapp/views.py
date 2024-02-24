from django.utils.crypto import get_random_string
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def my_view(request):
    data = request.data
    print(data)

    # idが"3"のTestモデルのインスタンスを取得
    test_instance = Test.objects.get(id="3")

    # パスワードをランダムな文字列に更新
    new_password = get_random_string(length=12)  # 12文字のランダムな文字列を生成
    test_instance.password = new_password
    test_instance.save()

    # 更新後のTestモデルの全レコードをシリアライズして出力
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
