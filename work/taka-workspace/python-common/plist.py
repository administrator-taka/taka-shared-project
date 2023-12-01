import lxml.etree as ET

file_root = 'ダウンロードまでのパス'

# plistファイルのパス
plist_file_path = file_root+'Downloads/test.plist'

# plistファイルをバイナリモードで読み込む
with open(plist_file_path, 'rb') as file:
    xml_data = file.read()

# ElementTreeオブジェクトを作成
root = ET.fromstring(xml_data)

# 辞書情報を格納するリスト
plist_list = []

# 配列内の各辞書を処理
for dictionary in root.xpath('//array/dict'):
    phrase = dictionary.xpath(
        './key[text()="phrase"]/following-sibling::string')[0].text
    shortcut = dictionary.xpath(
        './key[text()="shortcut"]/following-sibling::string')[0].text

    # 辞書情報を辞書としてリストに追加
    plist_list.append({'phrase': phrase, 'shortcut': shortcut})


# 既存のテキストファイルのパス
existing_text_file_path = file_root+'Downloads/output1.txt'

# テキストファイルをバイナリモードで読み込む
with open(existing_text_file_path, 'rb') as existing_text_file:
    existing_content = existing_text_file.read()

# 出力ファイルのパス
output_file_path = file_root+'Downloads/output.txt'

# リストの内容を既存のテキストファイルに追記
with open(output_file_path, 'ab') as output_file:
    # 既存の内容を書き込む
    output_file.write(existing_content)

    # plist_list の内容を追記
    for item in plist_list:
        # UTF-16 LEに変換して書き込む
        output_file.write(
            f"{item['shortcut']}\t{item['phrase']}\t短縮よみ\n".encode('UTF-16 LE'))
