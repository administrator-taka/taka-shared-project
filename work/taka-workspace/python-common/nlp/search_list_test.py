# subtitles = []
# subtitles.append({"subtitle_text": "a", "test": 1})
# subtitles.append({"subtitle_text": "b", "test": 2})
# subtitles.append({"subtitle_text": "c", "test": 3})
# subtitles.append({"subtitle_text": "d", "test": 4})
# subtitles.append({"subtitle_text": "e", "test": 5})
# subtitles.append({"subtitle_text": "f", "test": 6})
# subtitles.append({"subtitle_text": "g", "test": 7})
# subtitles.append({"subtitle_text": "h", "test": 8})
# subtitles.append({"subtitle_text": "i", "test": 9})
# subtitles.append({"subtitle_text": "j", "test": 10})
# search_word = "f g h"
# search_word_list = search_word.split()
# n = len(search_word_list)
#
# for i in range(n - 1, len(subtitles)):
#     print("★★★")
#     target_word_list = []
#     for j in range(n):
#         subtitle = subtitles[i - (n - j - 1)]
#         target_word_list.append(subtitle["subtitle_text"])
#         print(target_word_list)
#     target_word = ' '.join(target_word_list)
#
#     if target_word in search_word:
#         print(subtitles[i - (n - 1)])
#         print(subtitles[i])


subtitles = [
    {"subtitle_text": "a", "test": 1},
    {"subtitle_text": "b", "test": 2},
    {"subtitle_text": "c", "test": 3},
    {"subtitle_text": "d", "test": 4},
    {"subtitle_text": "e", "test": 5},
    {"subtitle_text": "f", "test": 6},
    {"subtitle_text": "g", "test": 7},
    {"subtitle_text": "h", "test": 8},
    {"subtitle_text": "i", "test": 9},
    {"subtitle_text": "j", "test": 10}
]

search_word = "f g h"
search_word_list = search_word.split()
n = len(search_word_list)

for i in range(n - 1, len(subtitles)):
    target_word_list = [subtitles[i - (n - j - 1)]["subtitle_text"] for j in range(n)]
    target_word = ' '.join(target_word_list)

    if target_word == search_word:
        print(f"Match found: {subtitles[i - (n - 1)]} to {subtitles[i]}")
