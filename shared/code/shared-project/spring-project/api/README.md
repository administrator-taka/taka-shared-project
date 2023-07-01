参考資料
https://qiita.com/A-Kira/items/beaf79a0d39d9839e61e

shared-project/docker配下で  
cd ../../docker

```
docker compose down
docker compose build
docker compose up -d
docker-compose exec java bash

```

中に入ったら

```
cd api
./gradlew build
java -jar build/libs/api-0.0.1-SNAPSHOT.jar

```

http://localhost:8080/

にアクセスしてHelloWorldと表示されればOK