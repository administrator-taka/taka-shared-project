
import instaloader

from save_to_csv import save_to_csv
from settings import PASSWORD, TARGET_USERNAME, INSTAGRAM_USERNAME


def get_instagram_friends(username, password, target_username):
    # インスタンスを作成
    instaloader_instance = instaloader.Instaloader()

    # ログイン
    instaloader_instance.login(username, password)

    # 対象ユーザーのプロフィールを読み込み
    target_profile = instaloader.Profile.from_username(instaloader_instance.context, target_username)

    # フォローしているユーザーのリストを取得
    following = set(target_profile.get_followees())

    # フォロワーのリストを取得
    followers = set(target_profile.get_followers())

    # フォローしているがフォロワーにはいないユーザーを抽出
    not_followed_back = following - followers

    # フォロワーだがフォローしていないユーザーを抽出
    not_following_back = followers - following

    # フォロワーでもフォローしているユーザーでもないユーザーを抽出
    other_users = followers - not_followed_back - not_following_back

    # ユーザーごとのデータを抽出
    not_followed_back_user_data = [
        (user.username, user.full_name, '×', f'https://www.instagram.com/{user.username}', '〇', '×') for user in
        not_followed_back]
    not_following_back_user_data = [
        (user.username, user.full_name, '×', f'https://www.instagram.com/{user.username}', '×', '〇') for user in
        not_following_back]
    other_users_data = [(user.username, user.full_name, '×', f'https://www.instagram.com/{user.username}', '×', '×') for
                        user in other_users]

    # CSVファイルに書き込むデータを結合
    data = [
        ['ユーザー名', 'フルネーム', '削除フラグ', 'プロフィールリンク', 'フォローしているがフォローされていない', 'フォローされているがフォローしていない'],
        *not_followed_back_user_data,
        *not_following_back_user_data,
        *other_users_data
    ]

    return data


def main():
    # 仮アカウントのユーザー名とパスワードを設定
    username = INSTAGRAM_USERNAME
    password = PASSWORD

    # 対象のユーザー名
    target_username = TARGET_USERNAME

    # データを取得
    data = get_instagram_friends(username, password, target_username)

    # ファイル名
    filename = "instagram_friends.csv"

    # CSVファイルにデータを保存
    save_to_csv(data, filename)


if __name__ == "__main__":
    main()
