from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['POST'])
def my_view(request):
    data = request.data
    print(data)
    # データベースから値を取得する処理を実装する
    return Response("Response from API")


from rest_framework.viewsets import ModelViewSet
from .models import MyModel
from .serializer import MyModelSerializer


class MyModelViewSet(ModelViewSet):
    queryset = MyModel.objects.all()
    serializer_class = MyModelSerializer
