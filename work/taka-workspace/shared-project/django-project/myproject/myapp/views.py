import time

from django.db import transaction
from django.http import HttpResponseServerError
from django.utils.crypto import get_random_string
from rest_framework.decorators import api_view
from rest_framework.response import Response

from myproject.settings.base import YOUTUBE_API_KEY
from .logic.youtube_data_api import get_youtube_video_details, get_youtube_channel_details, get_all_playlist_videos


# APIビューを定義
@api_view(['POST'])
def my_view(request):
    print("テスト出力")
    print(YOUTUBE_API_KEY)
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

    try:
        # トランザクションを開始
        with transaction.atomic():
            insert_playlist("PL-f9rLhac0DErB5rSnM0iKvNqkLP8B22h")
    except Exception as e:
        # エラーが発生した場合は、ロールバックされる
        # エラーの詳細をログに記録することもできる
        print("An error occurred:", str(e))
        # エラーをクライアントに返す場合は、適切なHTTPレスポンスを返す
        return HttpResponseServerError("An error occurred while processing the request")

    # シリアライズされたデータをレスポンスとして返す
    return Response(serializer.data)


from tqdm import tqdm


def insert_playlist(playlist_id):
    response_data = get_all_playlist_videos(playlist_id)

    # プレイリスト内の各ビデオのIDを出力
    items = response_data
    processed_videos = 0

    # tqdm を使用して処理の進行状況を表示
    for item in tqdm(items, desc="Inserting videos", unit="video"):
        playlist_video_id = item.get("id")
        published_at = item.get("snippet").get("publishedAt")
        video_id = item.get("snippet").get("resourceId").get("videoId")

        # DBに既に同じセットが存在するかをチェック
        if PlaylistDetail.objects.filter(playlist_id=playlist_id, video_id=video_id).exists():
            print(f"Playlist detail for video {video_id} already exists. Skipping insertion.")
            continue

        # ビデオデータをシリアライズしてデータベースに挿入
        video_data = {
            "playlist_id": playlist_id,
            "video_id": video_id,
            "playlist_video_id": playlist_video_id,
            "published_at": published_at,
            "delete_flag": False  # デフォルト値を設定
        }
        serializer = PlaylistDetailSerializer(data=video_data)
        if serializer.is_valid():
            serializer.save()
            processed_videos += 1
        else:
            print("Failed to serialize video data:", serializer.errors)
        insert_video(video_id, item)


def insert_video(video_id, item):
    video_data = item

    # チャンネルのIDを取得
    channel_id = video_data["snippet"].get("channelId")
    if not channel_id:
        print("Channel ID not found.")
        return

    # チャンネルの詳細情報をチェックし、存在しない場合は挿入
    try:
        channel_detail = ChannelDetail.objects.get(channel_id=channel_id)
    except ChannelDetail.DoesNotExist:
        channel_data = get_youtube_channel_details(channel_id)["items"][0]
        insert_channel_detail(channel_data)

    try:
        video_detail = VideoDetail.objects.get(video_id=video_id)
    except VideoDetail.DoesNotExist:
        insert_video_detail(video_id,video_data)


def insert_channel_detail(channel_data):
    try:
        snippet = channel_data["snippet"]
    except (KeyError, IndexError):
        print("Channel data not found.")
        return

    channel_detail = ChannelDetail(
        channel_id=channel_data.get("id"),
        title=snippet.get("title"),
        description=snippet.get("description"),
        custom_url=snippet.get("customUrl"),
        published_at=snippet.get("publishedAt"),
        thumbnails=snippet.get("thumbnails"),
        # thumbnails=thumbnails_json,
        country=snippet.get("country"),
        delete_flag=False
    )
    channel_detail.save()
    print("Channel detail inserted successfully.")


def insert_video_detail(video_id,video_data):
    try:
        snippet = video_data["snippet"]
    except (KeyError, IndexError):
        print("Video data not found.")
        return

    video_detail = VideoDetail(
        video_id=video_id,
        title=snippet.get("title"),
        description=snippet.get("description"),
        thumbnails=snippet.get("thumbnails"),
        video_owner_channel_title=snippet.get("videoOwnerChannelTitle"),
        video_owner_channel_id=snippet.get("videoOwnerChannelId"),
        delete_flag=False
    )
    video_detail.save()
    print("Video detail inserted successfully.")


from rest_framework.viewsets import ModelViewSet
from .models import Test, ChannelDetail, VideoDetail, PlaylistDetail
from .serializer import TestSerializer, PlaylistDetailSerializer


# モデルビューセットを定義
class TestViewSet(ModelViewSet):
    # 全てのTestモデルのクエリセットを取得
    queryset = Test.objects.all()
    # Testモデル用のシリアライザクラスを指定
    serializer_class = TestSerializer
