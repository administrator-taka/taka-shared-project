import yt_dlp
import os
def download_subtitle_vtt(video_id: str, lang: str) -> str:
    """指定したYouTubeビデオの字幕ファイルをダウンロードする

    Args:
        video_id (str): YouTubeのビデオID
        lang (str): 字幕の言語コード（例: 'en'）
    Returns:
        str: 字幕の内容
    """
    try:
        # yt_dlpのオプションを設定
        options = {
            'writesubtitles': True,  # 字幕を書き出す
            'writeautomaticsub': True,  # 自動生成字幕を書き出す
            'skip_download': True,  # ダウンロードをスキップ
            'subtitleslangs': [lang],  # 字幕の言語を指定
            'outtmpl': f'./{video_id}.%(ext)s',  # 出力パスのテンプレート
        }

        # yt_dlpのメイン関数を呼び出してダウンロード
        with yt_dlp.YoutubeDL(options) as ydl:
            ydl.download(['https://youtu.be/' + video_id])

        # ダウンロードしたファイルのパス
        file_path = f'./{video_id}.{lang}.vtt'

        # ファイルが存在するか確認して、内容を取得
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as file:
                subtitles_content = file.read()

            return subtitles_content
        else:
            print(f'字幕ファイルが見つかりませんでした: {file_path}')
            return ''
    except Exception as e:
        # 例外が発生した場合は、エラーを出力する
        print(f'エラーが発生しました: {e}')
        return ''
    finally:
        # ファイルが存在する場合は削除
        if os.path.exists(file_path):
            os.remove(file_path)


# ビデオIDと言語コードを指定して字幕をダウンロード
subtitles_content = download_subtitle_vtt('D7QBJ73rC9M', 'ja')

# 字幕の内容を表示
print(subtitles_content)
