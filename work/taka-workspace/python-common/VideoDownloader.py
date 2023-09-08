import settings
from yt_dlp import YoutubeDL

# VideoDownloaderクラスの定義
class VideoDownloader:
    def __init__(self):
        # FFMPEG_PATHを設定ファイルから取得
        ffmpeg_location = settings.FFMPEG_PATH
        if not ffmpeg_location:
            # FFMPEG_PATHが設定されていない場合、エラーメッセージを表示してydl_optsをNoneに設定
            print("FFMPEG_LOCATIONが設定されていません。デフォルトのパスまたはエラーハンドリングを行ってください。")
            self.ydl_opts = None
        else:
            # FFMPEG_PATHが設定されている場合、ydl_optsを設定
            self.ydl_opts = {
                'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best',
                'outtmpl': None,
                'ffmpeg_location': ffmpeg_location,
            }

    # 動画をMP4形式でダウンロードするメソッド
    def download_video_mp4(self, video_id, output_path):
        if self.ydl_opts is None:
            # FFMPEG_LOCATIONが設定されていない場合、エラーメッセージを表示してダウンロードを中止
            print("FFMPEG_LOCATIONが設定されていないため、ダウンロードできません。")
            return

        # ダウンロード対象のYouTube URLを生成
        URL = ["https://www.youtube.com/watch?v=" + video_id]

        # タイムスタンプのトリミングを無効にする
        self.ydl_opts.update({'postprocessor_args': []})

        # 出力ファイルパスを設定
        self.ydl_opts['outtmpl'] = output_path + '.%(ext)s'

        try:
            with YoutubeDL(self.ydl_opts) as ydl:
                ydl.download(URL)
        except Exception as e:
            # ダウンロード中にエラーが発生した場合、エラーメッセージを表示
            print('ビデオのダウンロード中にエラーが発生しました:')
            print(e)
        print('download_video_mp4 end')

# メインスクリプトのエントリーポイント
if __name__ == "__main__":
    video_id = "4rDOsvzTicY"
    output_path = "./"+video_id

    # VideoDownloaderクラスのインスタンスを作成
    downloader = VideoDownloader()
    
    # 動画をダウンロードするメソッドを呼び出し
    downloader.download_video_mp4(video_id, output_path)
