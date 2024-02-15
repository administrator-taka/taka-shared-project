import os
import aspose.words as aw

# フォルダのパス
folder_path = r'test/Violet Evergarden Subtitle'

# フォルダ内のすべての.拡張子ファイルを削除
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.pdf'):
            docx_file_path = os.path.join(root, file)
            try:
                # ファイルを削除
                os.remove(docx_file_path)
                print(f"Deleted {file}")
            except Exception as e:
                print(f"Failed to delete {file}: {str(e)}")
