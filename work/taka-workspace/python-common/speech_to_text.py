import speech_recognition as sr
from pydub import AudioSegment
import os

def transcribe_mp3_to_text(mp3_file):
    # MP3ファイルを読み込み、一時ファイルとしてWAV形式に変換
    audio = AudioSegment.from_mp3(mp3_file)
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

    return text

# 使用例
mp3_file = "001.mp3"
result_text = transcribe_mp3_to_text(mp3_file)
print("文字起こし結果:", result_text)
