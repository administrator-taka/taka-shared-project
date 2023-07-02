参考資料
https://qiita.com/A-Kira/items/beaf79a0d39d9839e61e

dev環境用

```
docker compose down
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
./gradlew build
java -jar build/libs/mywebapp-0.0.1-SNAPSHOT.jar

```

これは必要なのかわからない

```
docker rmi shared-project-java
docker compose build

```

http://localhost:8080/
がルート