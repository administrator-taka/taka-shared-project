import os


def get_folder_size(folder_path):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            total_size += os.path.getsize(file_path)
    return total_size


def format_size(size):
    # バイト数を人間が読みやすい形式に変換
    for unit in ['bytes', 'KB', 'MB', 'GB', 'TB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0


def list_folder_sizes(root_folder):
    folder_sizes = {}
    for dirpath, dirnames, filenames in os.walk(root_folder):
        folder_size = get_folder_size(dirpath)
        folder_sizes[dirpath] = folder_size

    total_size = sum(folder_sizes.values())
    print("全体のサイズ:", format_size(total_size))
    print("\n各フォルダのサイズ:")
    for folder_path, size in folder_sizes.items():
        print(f"{folder_path}: {format_size(size)}")


if __name__ == "__main__":
    path = r"ここにパスを入れる"
    if os.path.exists(path):
        list_folder_sizes(path)
    else:
        print("指定されたパスが存在しません。")
