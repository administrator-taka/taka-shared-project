import json

import pandas as pd

# ローカルのHTMLファイルを指定
html_file = 'test/Violet Evergarden Subtitle Copy/Violet Evergarden E.01/Violet Evergarden E.01 (ENG dub).html'

# HTMLからテーブルを読み込む
tables = pd.read_html(html_file, header=0, encoding='utf-8')

# 空の配列を用意
filtered_values = []

# 例えば、最初のテーブルを取得する場合
df = tables[0]

for index, row in df.iterrows():
    # for column, value in row.items():
    # すべての列の値を結合して代入
    value = ':'.join(str(cell) for cell in row if pd.notna(cell))

    if value:  # 空の場合は追加しない
        starts_with_narration = value.startswith('(Narration)')
        starts_with_flashback = value.startswith('(Flashback)')
        starts_and_ends_with_bracket = value.startswith('[') and value.endswith(']')

        if not starts_and_ends_with_bracket:
            filtered_values.append(value)  # 条件に合致する要素を配列に追加

# # print(len(filtered_values))
# # 配列に追加された値を出力
# for value in filtered_values:
#     print(value)
# データフレームを作成
data = {'英文': filtered_values,
        '日本語訳': [''] * len(filtered_values),  # 直訳カラムの初期値は空文字列とする
        '単語リスト': [''] * len(filtered_values)}  # 単語リストカラムの初期値は空文字列とする
df_new = pd.DataFrame(data)

# 例文
# csv形式の英文に日本語訳と単語リストのデータを追加してほしい。
# 英文,日本語訳,単語リスト
# "The children have eaten all the apples.","子供たちはリンゴを全部食べた。","children(child):子供, eaten(eat):食べる, apples(apple):リンゴ"
# これに従って下記のcsvを完成させてコードスペースに出力して。


# CSVに出力
output_csv_file = 'output.csv'
df_new.to_csv(output_csv_file, index=False)
print(f"CSVファイル '{output_csv_file}' に出力しました。")

# # JSONファイルに出力
# output_json_file = 'output.json'
# with open(output_json_file, 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)
# print(f"JSONファイル '{output_json_file}' に出力しました。")