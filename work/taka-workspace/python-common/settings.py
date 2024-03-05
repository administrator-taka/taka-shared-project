from decouple import config

FFMPEG_PATH = config('FFMPEG_PATH', default='/デフォルトのffmpegのパス')
YOUTUBE_API_KEY = config('YOUTUBE_API_KEY')
