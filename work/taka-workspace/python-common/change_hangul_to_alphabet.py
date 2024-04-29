from hangul_utils import split_syllables

def convert_to_alphabet(korean_text):
    syllables = split_syllables(korean_text)
    alphabet_text = ""
    for syllable in syllables:
        if syllable == " ":
            alphabet_text += " "
        else:
            alphabet_text += syllable
    # 韓国語のアルファベット表現を持つ辞書
    korean_alphabet = {
        'ㄱ': 'g', 'ㄲ': 'kk', 'ㄴ': 'n', 'ㄷ': 'd', 'ㄸ': 'tt', 'ㄹ': 'r', 'ㅁ': 'm',
        'ㅂ': 'b', 'ㅃ': 'pp', 'ㅅ': 's', 'ㅆ': 'ss', 'ㅇ': '', 'ㅈ': 'j', 'ㅉ': 'jj',
        'ㅊ': 'ch', 'ㅋ': 'k', 'ㅌ': 't', 'ㅍ': 'p', 'ㅎ': 'h', 'ㅏ': 'a', 'ㅐ': 'ae',
        'ㅑ': 'ya', 'ㅒ': 'yae', 'ㅓ': 'eo', 'ㅔ': 'e', 'ㅕ': 'yeo', 'ㅖ': 'ye',
        'ㅗ': 'o', 'ㅘ': 'wa', 'ㅙ': 'wae', 'ㅚ': 'oe', 'ㅛ': 'yo', 'ㅜ': 'u',
        'ㅝ': 'wo', 'ㅞ': 'we', 'ㅟ': 'wi', 'ㅠ': 'yu', 'ㅡ': 'eu', 'ㅢ': 'ui',
        'ㅣ': 'i', ' ': ' '
    }

    # 韓国語のテキストをアルファベットに変換
    alphabet_text = ''
    for char in syllables:
        alphabet_text += korean_alphabet.get(char, char)
    return alphabet_text


# Example usage
# korean_text = "안녕하세요"
korean_text = "뭐라 해야 되지"
alphabet_text = convert_to_alphabet(korean_text)
print(alphabet_text)
