from rest_framework.views import APIView
from rest_framework.response import Response
from myapp.models import Test  # TestSerializer を myapp.models からインポートする
from myapp.serializer import TestSerializer  # ここを修正

class TestAPIView(APIView):
    def post(self, request):
        # POSTリクエストからデータを受け取ります
        data = request.data

        # 受け取ったデータを使ってデータベースから値を取得します
        test_object = Test.objects.filter(id=data.get('id')).first()

        # データベースから取得した値をシリアライズします
        serializer = TestSerializer(test_object)

        # シリアライズされたデータをJSONレスポンスとして返します
        return Response(serializer.data)
