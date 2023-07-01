FROM openjdk:17-slim

# 必要なパッケージやツールのインストールなどを行います

WORKDIR /srv

# 必要なファイルやディレクトリをコンテナ内にコピーします
COPY ../spring-project /srv/spring-project

# コンテナ内での作業ディレクトリを指定します
WORKDIR /srv/spring-project/mywebapp

# 依存関係のインストールやビルドなど、必要なコマンドを実行します
RUN ./gradlew build

# コンテナの起動時に実行されるコマンドを指定します
CMD java -jar build/libs/mywebapp-0.0.1-SNAPSHOT.jar
