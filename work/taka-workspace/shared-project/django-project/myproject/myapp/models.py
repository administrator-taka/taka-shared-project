# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Test(models.Model):
    id = models.CharField(primary_key=True, max_length=50)
    name = models.CharField(max_length=50, blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test'


from django.db import models

class ChannelDetail(models.Model):
    channel_id = models.CharField(primary_key=True, max_length=100)  # チャンネルID
    title = models.CharField(max_length=100, null=True)  # チャンネルのタイトル
    description = models.TextField(null=True)  # チャンネルの説明
    custom_url = models.CharField(max_length=100, null=True)  # カスタムURL
    published_at = models.DateTimeField(null=True)  # チャンネルの作成日時
    thumbnails = models.JSONField(null=True)  # サムネイル画像のURLをJSON形式で保存
    country = models.CharField(max_length=2, null=True)  # チャンネルが所在する国のISO 3166-1 国コード
    delete_flag = models.BooleanField(default=False)  # レコード削除フラグ、デフォルトは False

    class Meta:
        db_table = 'channel_detail'  # テーブル名の指定


class VideoDetail(models.Model):
    video_id = models.CharField(primary_key=True, max_length=100)  # video_id は文字列として最大100文字
    title = models.CharField(max_length=200, null=True)  # 動画のタイトル
    description = models.TextField(null=True)  # 動画の説明
    thumbnails = models.JSONField(null=True)  # サムネイル画像のURLをJSON形式で保存
    video_owner_channel_title = models.CharField(max_length=200, null=True)  # チャンネルのタイトル
    video_owner_channel_id = models.CharField(max_length=100, null=True)  # チャンネルID
    delete_flag = models.BooleanField(default=False)  # レコード削除フラグ、デフォルトは False

    class Meta:
        db_table = 'video_detail'  # テーブル名の指定


class PlaylistDetail(models.Model):
    playlist_id = models.CharField(max_length=100)  # プレイリストID
    video_id = models.CharField(max_length=100)  # 動画ID
    playlist_video_id = models.CharField(max_length=100)  # プレイリスト内の動画ID
    published_at = models.DateTimeField(null=True)  # 動画の登録日時
    delete_flag = models.BooleanField(default=False)  # レコード削除フラグ、デフォルトは False

    class Meta:
        db_table = 'playlist_detail'  # テーブル名の指定
        unique_together = [['playlist_id', 'playlist_video_id']]  # 重複を許さない組み合わせを指定
