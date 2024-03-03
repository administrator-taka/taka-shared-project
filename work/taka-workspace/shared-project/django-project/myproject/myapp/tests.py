from myapp.logic.youtube_data_api import get_youtube_video_details, get_youtube_channel_details, \
     get_all_playlist_videos
from myproject.settings.base import YOUTUBE_API_KEY
import json

if __name__ == "__main__":
    print("テスト出力")
    print(YOUTUBE_API_KEY)

    # response_data = get_youtube_video_details("xu87Lm9-ztU")
    #
    # # JSONデータを整形して出力
    # formatted_json = json.dumps(response_data, indent=4, ensure_ascii=False)
    # print(formatted_json)

    # response_data = get_youtube_channel_details("UCIdEIHpS0TdkqRkHL5OkLtA")
    #
    # # JSONデータを整形して出力
    # formatted_json = json.dumps(response_data, indent=4, ensure_ascii=False)
    # print(formatted_json)

    # response_data = get_all_playlist_videos("UUIdEIHpS0TdkqRkHL5OkLtA")
    #
    # # JSONデータを整形して出力
    # formatted_json = json.dumps(response_data, indent=4, ensure_ascii=False)
    # print(formatted_json)
