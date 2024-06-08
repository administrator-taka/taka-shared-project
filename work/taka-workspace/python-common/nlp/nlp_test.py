# import nltk
# from nltk.corpus import stopwords
#
# nltk.download('stopwords')
# stop_words = set(stopwords.words('english'))
#
# # サンプルの文字列
# text = "This is a sample sentence, showing off the stop words filtration."
#
# # 文字列を単語に分割
# words = text.split()
#
# # ストップワードを除外
# filtered_words = [word for word in words if word.lower() not in stop_words]
# print(filtered_words)


from konlpy.corpus import kobill
from konlpy.tag import Okt

# Okt (Open Korean Text) 객체を初期化
okt = Okt()

# 韓国語のストップワードリストを取得
stop_words = kobill.words('stopwords.txt')

# サンプルの文字列
text = "국회법 제10조 제3항에 따라 국회는 월 1회 이상의 회기를 열며, 국정감사·행정안전 및 기타 국회의 의무에 관한 사항에 대하여는 국회재적의원 4분의 1 이상의 출석과 출석의원 과반수의 찬성으로 의결한다."

# 형태소 분석하여 명사만 추출
words = okt.nouns(text)

# 스톱워드를 제외
filtered_words = [word for word in words if word not in stop_words]
print(filtered_words)
