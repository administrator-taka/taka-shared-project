import asyncio
import os
from pyppeteer import launch

async def convert_html_to_pdf(html_file_path, output_pdf_path):
    browser = await launch(headless=True)
    page = await browser.newPage()
    await page.goto(f'file://{os.path.abspath(html_file_path)}', waitUntil='networkidle0')
    # フォントの設定
    await page.pdf({'path': output_pdf_path, 'format': 'A4', 'fontOptions': {'defaultEncoding': 'utf-8'}})
    await browser.close()
    print(f"Converted {html_file_path} to PDF")


def batch_convert_html_to_pdf(folder_path):
    # フォルダ内のすべてのHTMLファイルを処理する
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.html'):
                html_file_path = os.path.join(root, file)
                output_pdf_path = os.path.splitext(html_file_path)[0] + '.pdf'
                try:
                    # HTMLファイルをPDFに変換
                    asyncio.get_event_loop().run_until_complete(convert_html_to_pdf(html_file_path, output_pdf_path))
                except Exception as e:
                    print(f"Failed to convert {html_file_path} to PDF: {str(e)}")

# フォルダのパス
folder_path = r'test/Violet Evergarden Subtitle'

# すべてのHTMLファイルをPDFに変換する
batch_convert_html_to_pdf(folder_path)
