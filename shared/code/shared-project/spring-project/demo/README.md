参考資料
https://qiita.com/A-Kira/items/beaf79a0d39d9839e61e

shared-project配下で

```
docker compose down
docker compose build
docker compose up -d

```

TODO: 変更を反映させる場合
```
docker-compose exec java bash

```

中に入ったら

```
cd demo
./gradlew build
java -jar build/libs/demo-0.0.1-SNAPSHOT.jar

```

http://localhost:8080/

にアクセスしてHelloWorldと表示されればOK