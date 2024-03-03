import requests
from myproject.settings.base import YOUTUBE_API_KEY


def get_youtube_video_details(video_id):
    api_url = "https://www.googleapis.com/youtube/v3/videos"

    # GETリクエストのパラメータを設定
    params = {
        'id': video_id,
        'key': YOUTUBE_API_KEY,
        'part': 'snippet,liveStreamingDetails'
    }

    # YouTube Data API を呼び出してレスポンスを取得
    return make_api_request(api_url, params)


def get_youtube_channel_details(channel_id):
    api_url = "https://www.googleapis.com/youtube/v3/channels"

    # GETリクエストのパラメータを設定
    params = {
        'id': channel_id,
        'key': YOUTUBE_API_KEY,
        'part': 'snippet'
    }

    # YouTube Data API を呼び出してレスポンスを取得
    return make_api_request(api_url, params)


def get_all_playlist_videos(playlist_id):
    all_videos = []

    # 初回のリクエスト
    first_response = get_playlist_videos_page(playlist_id)

    # 最初のリクエストが成功した場合
    if first_response is not None:
        # 結果をリストに追加
        all_videos.extend(first_response["items"])

        # 次のページがある場合、再帰的にリクエスト
        next_page_token = first_response.get("nextPageToken")
        while next_page_token:
            next_response = get_playlist_videos_page(playlist_id, page_token=next_page_token)
            if next_response is not None:
                all_videos.extend(next_response["items"])
                next_page_token = next_response.get("nextPageToken")
            else:
                break

    return all_videos


def get_playlist_videos_page(playlist_id, page_token=None):
    api_url = "https://www.googleapis.com/youtube/v3/playlistItems"

    # GETリクエストのパラメータを設定
    params = {
        'playlistId': playlist_id,
        'key': YOUTUBE_API_KEY,
        'part': 'snippet',
        'maxResults': 50
    }

    # ページトークンが指定されている場合は追加
    if page_token:
        params['pageToken'] = page_token

    # YouTube Data API を呼び出してレスポンスを取得
    return make_api_request(api_url, params)


def make_api_request(api_url, params):
    try:
        # GETリクエストを送信してレスポンスを取得
        response = requests.get(api_url, params=params)

        # レスポンスのステータスコードを確認
        if response.status_code == 200:
            # JSON形式のレスポンスを解析して返す
            return response.json()
        else:
            # エラーメッセージを出力してNoneを返す
            print("Error:", response.status_code)
            return None
    except Exception as e:
        # 例外が発生した場合はエラーメッセージを出力してNoneを返す
        print("Error:", str(e))
        return None
