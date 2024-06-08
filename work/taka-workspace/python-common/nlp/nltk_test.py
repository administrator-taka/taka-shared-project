import nltk
from nltk.tokenize import sent_tokenize

# ファイルからテキストを読み込み
with open('../test/test_text.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# 必要なデータをダウンロード
nltk.download('punkt')

# 分割
sentences = sent_tokenize(text)
for sentence in sentences:
    print(sentence)

import spacy

# python -m spacy download en_core_web_sm
# spaCyの言語モデルをロード
nlp = spacy.load("en_core_web_sm")

# 分割
doc = nlp(text)
sentences = list(doc.sents)
for sentence in sentences:
    print(sentence)


# from transformers import pipeline
#
# # 分割
# nlp = pipeline("sentiment-analysis")
# results = nlp(text)
#
# # 結果の表示
# for result in results:
#     print(result)