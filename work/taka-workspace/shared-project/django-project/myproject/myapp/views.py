from django.utils.crypto import get_random_string
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .logic.Database import insert_video_detail


# APIビューを定義
@api_view(['POST'])
def my_view(request):
    # POSTリクエストのデータを取得
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

    # VideoDetail モデルにデータをインサート
    video_detail_data = {
        'video_id': 'your_fixed_video_id',
        'published_at': '2024-03-03T12:00:00Z',  # 例として固定の日時を使用
        'channel_id': 'your_fixed_channel_id',
        'title': 'Your Fixed Title',
        'thumbnails': 'https://example.com/default_thumbnail.jpg',
        'channel_title': 'Your Fixed Channel Title',
        'default_audio_language': 'en',
        'actual_start_time': '2024-03-03T12:00:00Z',  # 例として固定の日時を使用
        'actual_end_time': '2024-03-03T13:00:00Z',  # 例として固定の日時を使用
        'scheduled_start_time': '2024-03-03T12:00:00Z',  # 例として固定の日時を使用
        'delete_flag': False
    }
    insert_video_detail(video_detail_data)

    # シリアライズされたデータをレスポンスとして返す
    return Response(serializer.data)


from rest_framework.viewsets import ModelViewSet
from .models import Test
from .serializer import TestSerializer


# モデルビューセットを定義
class TestViewSet(ModelViewSet):
    # 全てのTestモデルのクエリセットを取得
    queryset = Test.objects.all()
    # Testモデル用のシリアライザクラスを指定
    serializer_class = TestSerializer
