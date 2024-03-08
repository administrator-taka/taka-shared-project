import csv


def save_to_csv(data, filename):
    # データをCSVファイルに書き込む
    with open(filename, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(data)

    print("CSVファイルにデータを書き込みました。")