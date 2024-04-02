import pandas as pd
from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    try:
        translated_text = translator.translate(text, dest=target_language, src='ko')
        print("翻訳中:", text)
        print("翻訳結果:", translated_text.text)
        return translated_text.text
    except Exception as e:
        print("翻訳中にエラーが発生しました:", e)
        return ""


def translate_column(csv_path, column_name, target_language, new_column_name):
    # CSVファイルを読み取り
    df = pd.read_csv(csv_path)

    # 新しい列を追加して翻訳
    df[new_column_name] = df[column_name].apply(lambda x: translate_text(x, target_language))

    # 結果をCSVファイルに保存
    df.to_csv(csv_path, index=False)

# 指定したパスのCSVファイルを読み取り、resultカラムの韓国語を日本語に翻訳してtransrateカラムを追加して更新
csv_path = "topik_60.csv"
column_name = "result"
target_language = "ja"  # 日本語
new_column_name = "transrate"
translate_column(csv_path, column_name, target_language, new_column_name)
