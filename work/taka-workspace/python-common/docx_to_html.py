import os
import mammoth

def convert_docx_to_html(docx_file_path, output_html_path):
    # 対象の`.docx`ファイルを開く
    with open(docx_file_path, "rb") as docx_file:
        # HTMLに変換
        result = mammoth.convert_to_html(docx_file)
        html = result.value

    # HTMLに罫線のCSSを追加
    html_with_css = add_table_borders(html)

    # HTMLをファイルに書き出す
    with open(output_html_path, mode="w", encoding="utf-8") as html_file:
        html_file.write(html_with_css)

def add_table_borders(html):
    # 表形式に罫線を追加するCSS
    css = """
    <style>
    table {
        border-collapse: collapse;
    }
    th, td {
        border: 1px solid black;
        padding: 8px;
        text-align: left;
    }
    </style>
    """
    # HTMLにCSSを追加して返す
    return css + html

def batch_convert_docx_to_html(folder_path):
    # フォルダ内のすべての`.docx`ファイルを処理する
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.docx'):
                docx_file_path = os.path.join(root, file)
                output_html_path = os.path.splitext(docx_file_path)[0] + '.html'
                try:
                    # `.docx`ファイルをHTMLに変換
                    convert_docx_to_html(docx_file_path, output_html_path)
                    print(f"Converted {file} to HTML")
                except Exception as e:

                    print(f"Failed to convert {file} to HTML: {str(e)}")

# フォルダのパス
folder_path = r'test/Violet Evergarden Subtitle'

# すべての`.docx`ファイルをHTMLに変換する
batch_convert_docx_to_html(folder_path)
