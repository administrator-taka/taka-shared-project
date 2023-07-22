参考資料
https://qiita.com/A-Kira/items/beaf79a0d39d9839e61e

dev環境用

```
docker compose down
docker-compose -f docker-compose.dev.yml down
docker-compose -f docker-compose.dev.yml up -d --build

```

shared-project配下で

```
docker compose down
docker compose up -d
docker-compose exec java bash

```

中に入ったら

```
cd mywebapp
./gradlew build -x test
java -jar build/libs/mywebapp-0.0.1-SNAPSHOT.jar

```

これは必要なのかわからない

```
docker rmi shared-project-java
docker compose build

```

http://localhost:8080/
がルート

ローカル用JDKインストール
https://corretto.aws/downloads/latest/amazon-corretto-17-x64-windows-jdk.msi
ここからAmazon Corretto 17のインストール

ファイル/プロジェクト構造/SDK/プラスボタンを押してC:\Program Files\Amazon Corretto\jdk17.0.8_7を選択して追加
プロジェクト/で17を選択し，corretto-17を選択するだったと思う．
mywebapp\src\main\java\com\example\mywebapp\MywebappApplication.javaを右クリックし実行