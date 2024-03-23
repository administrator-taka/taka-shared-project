import os
from pydub import AudioSegment
from pydub.silence import detect_silence
from mutagen.mp3 import MP3
from mutagen.easyid3 import EasyID3

# 元のフォルダのパス
folder_path = r"C:\Users\daiv3\Downloads\9784876153909ex\9784876153909-3\例文のみ"

# フォルダ内のすべてのファイルに対して処理を行う
for filename in os.listdir(folder_path):
    if filename.endswith(".mp3"):
        # 音声ファイルのパス
        input_file = os.path.join(folder_path, filename)

        # 音声ファイルを読み込む
        sound = AudioSegment.from_mp3(input_file)

        # 元のメタデータを取得
        audio = MP3(input_file, ID3=EasyID3)
        metadata = {key: audio[key][0] for key in audio.keys()}

        # 無音の部分を検出
        silence_ranges = detect_silence(sound, min_silence_len=500, silence_thresh=-40)

        # 無音の部分を削除
        for start, end in reversed(silence_ranges):
            sound = sound[:start] + sound[end:]

        # 元のメタデータをセット
        sound = sound.set_frame_rate(sound.frame_rate)

        # 出力ファイルのパス
        output_file = os.path.join(folder_path, f"{os.path.splitext(filename)[0]}.mp3")

        # 変換した音声ファイルを保存する（メタデータも含む）
        sound.export(output_file, format="mp3", tags=metadata)

        print(f"{filename} の変換が完了しました。")
