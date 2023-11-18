from enum import Enum
import hgtk

# 子音
shiin = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

# 母音
boin = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']

# パッチム
batchim = ['',  # 0番目はパッチム無し
           'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ',
           'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ', 'ㅐ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ',
           'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']



class 音(Enum):
    母音 = 1
    子音 = 2
    その他 = 0






def 母音か子音か(input_text):
    split_text = hgtk.text.decompose(input_text).replace('ᴥ', '')  # 'ᴥ'を空文字に置き換える
    end_character = split_text[-1][-1]  # decomposeの結果から最後の文字の末尾のみを取得

    if end_character in boin:
        return 音.母音
    elif end_character in shiin:
        return 音.子音
    else:
        return 音.その他




def です_예요_이에요(input_text):
    check = 母音か子音か(input_text)
    if check == 音.母音:
        return input_text + '예요', input_text + 'です'
    elif check == 音.子音:
        return input_text + '이에요', input_text + 'です'
    else:
        return False


def ですか_예요_이에요(input_text):
    check = 母音か子音か(input_text)
    if check == 音.母音:
        return input_text + '예요？', input_text + 'ですか？'
    elif check == 音.子音:
        return input_text + '이에요？', input_text + 'ですか？'
    else:
        return False

def です_입니다(input_text):
    return input_text + '입니다', input_text + 'です'

def ですか_입니까(input_text):
    return input_text + '입니까？', input_text + 'ですか？'


def は_는_은(input_text):
    check = 母音か子音か(input_text)
    if check == 音.母音:
        return input_text + '는', input_text + 'は'
    elif check == 音.子音:
        return input_text + '은', input_text + 'は'
    else:
        return False


def が_가_이(input_text):
    check = 母音か子音か(input_text)
    if check == 音.母音:
        return input_text + '가', input_text + 'が'
    elif check == 音.子音:
        return input_text + '이', input_text + 'が'
    else:
        return False

def ではありません_가_아니예요_이__아니예요(input_text):
    check = 母音か子音か(input_text)
    if check == 音.母音:
        return input_text + '가 아니예요', input_text + 'ではありません'
    elif check == 音.子音:
        return input_text + '이 아니예요', input_text + 'ではありません'
    else:
        return False

def に_에_時間_存在(input_text):
    return input_text + '에', input_text + 'に'

def に_에게_人_動物(input_text):
    return input_text + '에게', input_text + 'に'


def を_를_을(input_text):
    check = 母音か子音か(input_text)
    if check == 音.母音:
        return input_text + '를', input_text + 'を'
    elif check == 音.子音:
        return input_text + '을', input_text + 'を'
    else:
        return False


def も_도(input_text):
    return input_text + '도', input_text + 'も'

print(です_예요_이에요('학생'))
print(ですか_예요_이에요('한국어'))
print(です_입니다('한국어'))
print(ですか_입니까('한국어'))
print(は_는_은('오늘'))
print(が_가_이('가방'))
print(ではありません_가_아니예요_이__아니예요('한국 사람'))
print(に_에_時間_存在('학교'))
print(に_에게_人_動物('친구'))
print(を_를_을('친구'))
print(も_도('친구'))


