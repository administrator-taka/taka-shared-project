from pydub import AudioSegment, silence
import os


def split_mp3(input_file, output_folder):
    # オーディオファイルを読み込む
    audio = AudioSegment.from_mp3(input_file)

    # 無音の検出に関するパラメータ
    silence_threshold = -70  # 閾値を必要に応じて調整する
    min_silence_len = 1000  # 無音として認識する最小の無音の長さ（ミリ秒）

    # 音声と無音の部分を検出して分割する
    non_silent_ranges = silence.detect_nonsilent(audio, min_silence_len=min_silence_len, silence_thresh=silence_threshold)

    # 分割したオーディオを保存するフォルダが存在しない場合は作成する
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 分割したオーディオを保存する
    for i, (start, end) in enumerate(non_silent_ranges):
        segment = audio[start:end]
        output_file = os.path.join(output_folder, f"{i + 1:03d}.mp3")
        segment.export(output_file, format="mp3")


# 入力MP3ファイルと出力フォルダを指定
input_file = "C:/Users/daiv3/Downloads/60_TOPIK1_L.mp3"
output_folder = "output"

# MP3ファイルを分割する
split_mp3(input_file, output_folder)
