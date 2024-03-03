import json

from django.db import transaction
from django.http import HttpResponseServerError
from django.utils.crypto import get_random_string
from rest_framework.decorators import api_view
from rest_framework.response import Response

from myproject.settings.base import YOUTUBE_API_KEY
from .logic.database import insert_video_detail
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

    video_id = 'KjymxCpOZD8'
    try:
        # トランザクションを開始
        with transaction.atomic():
            insert_playlist("UUIdEIHpS0TdkqRkHL5OkLtA")
            insert_video(video_id)
    except Exception as e:
        # エラーが発生した場合は、ロールバックされる
        # エラーの詳細をログに記録することもできる
        print("An error occurred:", str(e))
        # エラーをクライアントに返す場合は、適切なHTTPレスポンスを返す
        return HttpResponseServerError("An error occurred while processing the request")

    # シリアライズされたデータをレスポンスとして返す
    return Response(serializer.data)


def insert_playlist(playlist_id):
    response_data = get_all_playlist_videos(playlist_id)

    # プレイリスト内の各ビデオのIDを出力
    items = response_data
    for item in items:
        playlist_video_id = item.get("id")
        published_at = item.get("snippet").get("publishedAt")
        video_id = item.get("snippet").get("resourceId").get("videoId")
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
        else:
            print("Failed to serialize video data:", serializer.errors)

def insert_video(video_id):
    # 動画の詳細情報を取得
    video_data = get_youtube_video_details(video_id)
    if "items" not in video_data or len(video_data["items"]) == 0:
        print("Video not found.")
        return

    if "items" not in video_data or len(video_data["items"]) == 0:
        print("Video not found.")
        return

    # チャンネルのIDを取得
    channel_id = video_data["items"][0]["snippet"].get("channelId")
    if not channel_id:
        print("Channel ID not found.")
        return

    # チャンネルの詳細情報をチェックし、存在しない場合は挿入
    try:
        channel_detail = ChannelDetail.objects.get(channel_id=channel_id)
    except ChannelDetail.DoesNotExist:
        channel_data = get_youtube_channel_details(channel_id)
        insert_channel_detail(channel_data)

    insert_video_detail(video_data)


def insert_channel_detail(channel_data):
    try:
        snippet = channel_data["items"][0]["snippet"]
    except (KeyError, IndexError):
        print("Channel data not found.")
        return

    thumbnails = snippet.get("thumbnails", {})
    thumbnails_json = {
        "default": thumbnails.get("default", {}).get("url"),
        "medium": thumbnails.get("medium", {}).get("url"),
        "high": thumbnails.get("high", {}).get("url")
    }

    channel_detail = ChannelDetail(
        channel_id=channel_data["items"][0].get("id"),
        title=snippet.get("title"),
        description=snippet.get("description"),
        published_at=snippet.get("publishedAt"),
        thumbnails=thumbnails_json,
        default_audio_language=snippet.get("defaultAudioLanguage"),  # デフォルトの音声言語を取得
        country=snippet.get("country"),
        delete_flag=False
    )
    channel_detail.save()
    print("Channel detail inserted successfully.")


def insert_video_detail(video_data):
    try:
        snippet = video_data["items"][0]["snippet"]
    except (KeyError, IndexError):
        print("Video data not found.")
        return

    thumbnails = snippet.get("thumbnails", {})
    thumbnails_json = {
        "default": thumbnails.get("default", {}).get("url"),
        "medium": thumbnails.get("medium", {}).get("url"),
        "high": thumbnails.get("high", {}).get("url")
    }

    try:
        live_streaming_details = video_data["items"][0]["liveStreamingDetails"]
    except (KeyError, IndexError):
        live_streaming_details = None  # live_streaming_detailsが存在しない場合はNoneを使用する

    video_detail = VideoDetail(
        video_id=video_data["items"][0].get("id"),
        published_at=snippet.get("publishedAt"),
        channel_id=snippet.get("channelId"),
        title=snippet.get("title"),
        thumbnails=thumbnails_json,
        default_audio_language=snippet.get("defaultAudioLanguage"),
        actual_start_time=live_streaming_details.get("actualStartTime") if live_streaming_details else None,
        actual_end_time=live_streaming_details.get("actualEndTime") if live_streaming_details else None,
        scheduled_start_time=live_streaming_details.get("scheduledStartTime") if live_streaming_details else None,
        delete_flag=False
    )
    video_detail.save()
    print("Video detail inserted successfully.")


from rest_framework.viewsets import ModelViewSet
from .models import Test, ChannelDetail, VideoDetail
from .serializer import TestSerializer, VideoDetailSerializer, ChannelDetailSerializer, PlaylistDetailSerializer


# モデルビューセットを定義
class TestViewSet(ModelViewSet):
    # 全てのTestモデルのクエリセットを取得
    queryset = Test.objects.all()
    # Testモデル用のシリアライザクラスを指定
    serializer_class = TestSerializer
