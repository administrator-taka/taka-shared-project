import os
import csv

from speech_to_text import transcribe_mp3_to_text

# 元のフォルダのパス
folder_path =  "output"

# CSVファイルのパス
csv_file_path = "topik_60.csv"

# CSVファイルを書き込みモードで開く
with open(csv_file_path, "w", newline="", encoding="utf-8") as csv_file:
    # CSVライターを作成
    csv_writer = csv.writer(csv_file)

    # ヘッダーを書き込む
    csv_writer.writerow(["fileName", "result"])

    # フォルダ内のすべてのファイルに対して処理を行う
    for filename in os.listdir(folder_path):
        if filename.endswith(".mp3"):
            # 音声ファイルのパス
            input_file = os.path.join(folder_path, filename)

            try:
                # テキスト結果を取得
                result_text = transcribe_mp3_to_text(input_file)
            except Exception as e:
                print(e)
                result_text=""
            # ファイル名とテキスト結果を表示
            print(f"ファイル名: {filename}, テキスト結果: {result_text}")

            # ファイル名とテキスト結果をCSVファイルに書き込む
            csv_writer.writerow([filename, result_text])

print("CSVファイルに出力が完了しました。")
