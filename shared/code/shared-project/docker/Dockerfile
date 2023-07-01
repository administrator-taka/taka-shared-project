FROM openjdk:17-slim

# 必要なパッケージやツールのインストールなどを行います

WORKDIR /srv

# 必要なファイルやディレクトリをコンテナ内にコピーします
COPY ../spring-project /srv/spring-project

# コンテナ内での作業ディレクトリを指定します
WORKDIR /srv/spring-project/demo

# 依存関係のインストールやビルドなど、必要なコマンドを実行します
RUN chmod +x ./gradlew && ./gradlew build

# コンテナの起動時に実行されるコマンドを指定します
CMD java -jar build/libs/demo-0.0.1-SNAPSHOT.jar
