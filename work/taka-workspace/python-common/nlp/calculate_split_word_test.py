subtitles = [
    {"subtitle_text": "a c k d", "test": 1},
    {"subtitle_text": "a s d k", "test": 2},
    {"subtitle_text": "y d k m", "test": 3},
    {"subtitle_text": "4 f v", "test": 4},
    {"subtitle_text": "z", "test": 5},
    {"subtitle_text": "o e c v", "test": 6},
]

min_word = 3
info_words = []  # 各infoの単語を一時的に収集するリストを初期化

def get_combinations(words, min_word):
    combinations = []
    for i in range(len(words) - min_word + 1):
        combination = ' '.join(words[i:i + min_word])
        combinations.append(combination)
    return combinations

for subtitle in subtitles:
    subtitle_text = subtitle["subtitle_text"]
    # 各字幕テキストを単語に分割し、リストに追加
    words = subtitle_text.split()
    join_words = get_combinations(words, min_word)  # min_wordごとの組み合わせで結合
    info_words.extend(join_words)

print(info_words)
