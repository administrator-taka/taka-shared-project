import speech_recognition as sr
from pydub import AudioSegment
import os

# MP3ファイルを読み込み、一時ファイルとしてWAV形式に変換
audio = AudioSegment.from_mp3("001.mp3")
temp_wav_file = "temp.wav"
audio.export(temp_wav_file, format="wav")

# 音声認識器のインスタンスを作成
recognizer = sr.Recognizer()

# WAVファイルの文字起こし
with sr.AudioFile(temp_wav_file) as source:
    audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data, language="ko-KR")

# 一時ファイルの削除
os.remove(temp_wav_file)

# 文字起こし結果の出力
print(text)
