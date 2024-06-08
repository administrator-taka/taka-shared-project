def is_staircase(subtitles):
    current_subtitle_text = None
    count = 0
    for subtitle in subtitles:
        if current_subtitle_text and subtitle["subtitle_text"].startswith(current_subtitle_text):
            count += 1
        current_subtitle_text = subtitle["subtitle_text"]

    ratio = count / len(subtitles)
    print(f"{count}/{len(subtitles)}={ratio}")
    if ratio > 0.5:
        return False
    return True


# テスト用データ
subtitles1 = [
    {"subtitle_text": "a", "test": 1},
    {"subtitle_text": "a b", "test": 2},
    {"subtitle_text": "a b c", "test": 3},
    {"subtitle_text": "a b c d", "test": 4},
    {"subtitle_text": "z", "test": 5},
    {"subtitle_text": "z x", "test": 6},
    {"subtitle_text": "z x c", "test": 7},
    {"subtitle_text": "z x c d", "test": 8},
    {"subtitle_text": "m", "test": 9},
    {"subtitle_text": "m t", "test": 10}
]

subtitles2 = [
    {"subtitle_text": "a c k d", "test": 1},
    {"subtitle_text": "a s d k", "test": 2},
    {"subtitle_text": "y d k m", "test": 3},
    {"subtitle_text": "4 f v", "test": 4},
    {"subtitle_text": "z", "test": 5},
    {"subtitle_text": "o e c v", "test": 6},
]

print("Subtitles1 is a staircase:", is_staircase(subtitles1))
print("Subtitles2 is a staircase:", is_staircase(subtitles2))
