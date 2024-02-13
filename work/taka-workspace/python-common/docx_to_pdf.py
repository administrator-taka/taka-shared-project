import os
import aspose.words as aw

# フォルダのパス
folder_path = r'C:\Users\xxxxx\xxx'

# フォルダ内のすべての.docxファイルをPDFに変換
for root, dirs, files in os.walk(folder_path):
    for file in files:
        if file.endswith('.docx'):
            docx_file_path = os.path.join(root, file)
            output_pdf_path = os.path.splitext(docx_file_path)[0] + '.pdf'
            try:
                # Load word document
                doc = aw.Document(docx_file_path)

                # Save as PDF
                doc.save(output_pdf_path)
                print(f"Converted {file} to PDF")
            except Exception as e:
                print(f"Failed to convert {file} to PDF: {str(e)}")

# # フォルダ内のすべての.docxファイルを削除
# for root, dirs, files in os.walk(folder_path):
#     for file in files:
#         if file.endswith('.docx'):
#             docx_file_path = os.path.join(root, file)
#             try:
#                 # ファイルを削除
#                 os.remove(docx_file_path)
#                 print(f"Deleted {file}")
#             except Exception as e:
#                 print(f"Failed to delete {file}: {str(e)}")
