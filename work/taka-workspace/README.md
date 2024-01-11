# taka-workspace

```
├─README.md
├─python-common
│ ├─.gitignore
│ ├─VideoDownloader.py
│ ├─korean.py
│ ├─plist.py
│ ├─requirements.txt
│ ├─sample.env
│ └─settings.py
└─shared-project
├─django-project
│ └─myproject
│ ├─.gitignore
│ ├─manage.py
│ ├─myapp
│ │ ├─**init**.py
│ │ ├─admin.py
│ │ ├─apps.py
│ │ ├─migrations
│ │ │ └─**init**.py
│ │ ├─models.py
│ │ ├─tests.py
│ │ └─views.py
│ ├─myproject
│ │ ├─**init**.py
│ │ ├─asgi.py
│ │ ├─settings.py
│ │ ├─urls.py
│ │ └─wsgi.py
│ └─requirements.txt
├─docker
│ ├─Dockerfile
│ ├─api
│ │ └─Dockerfile
│ ├─bat
│ │ ├─**\_**docker-delete.bat
│ │ ├─api.bat
│ │ ├─docker-compose-up.bat
│ │ └─docker-restart.bat
│ ├─db
│ │ ├─Dockerfile
│ │ ├─scripts
│ │ │ └─init.sh
│ │ └─sql
│ │ └─test.sql
│ ├─django
│ │ └─Dockerfile
│ └─view
│ └─Dockerfile
├─docker-compose.dev.yml
├─docker-compose.yml
├─spring-project
│ └─mywebapp
│ ├─.gitignore
│ ├─README.md
│ ├─build.gradle
│ ├─gradle
│ │ └─wrapper
│ │ ├─gradle-wrapper.jar
│ │ └─gradle-wrapper.properties
│ ├─gradlew
│ ├─gradlew.bat
│ ├─settings.gradle
│ └─src
│ ├─main
│ │ ├─java
│ │ │ └─com
│ │ │ └─example
│ │ │ └─mywebapp
│ │ │ ├─MywebappApplication.java
│ │ │ ├─application
│ │ │ │ ├─dto
│ │ │ │ │ └─TestDto.java
│ │ │ │ └─service
│ │ │ │ ├─TestService.java
│ │ │ │ └─TestServiceImpl.java
│ │ │ ├─domain
│ │ │ │ ├─code
│ │ │ │ │ └─LanguageType.java
│ │ │ │ ├─logic
│ │ │ │ │ └─TestLogic.java
│ │ │ │ └─model
│ │ │ │ └─TestModel.java
│ │ │ ├─infrastructure
│ │ │ │ ├─entity
│ │ │ │ │ └─TestEntity.java
│ │ │ │ └─mapper
│ │ │ │ └─TestMapper.java
│ │ │ └─presentation
│ │ │ ├─controller
│ │ │ │ └─TestController.java
│ │ │ ├─request
│ │ │ │ └─TestRequest.java
│ │ │ └─response
│ │ │ └─TestResponse.java
│ │ └─resources
│ │ ├─application-develop.yml
│ │ ├─application-local.yml
│ │ ├─application.properties
│ │ ├─application.yml
│ │ └─com
│ │ └─example
│ │ └─mywebapp
│ │ └─infrastructure
│ │ └─mapper
│ │ └─TestMapper.xml
│ └─test
│ ├─java
│ │ └─com
│ │ └─example
│ │ └─mywebapp
│ │ ├─MywebappApplicationTests.java
│ │ └─domain
│ │ └─logic
│ │ └─TestLogicTest.java
│ └─resources
│ ├─application.yml
│ └─sql
│ ├─create_tbl.sql
│ └─test.sql
├─tree.py
├─tree.txt
└─vue-project
└─my-vue-app
├─.browserslistrc
├─.env.develop
├─.env.local
├─.eslintrc.js
├─.gitignore
├─README.md
├─babel.config.js
├─package-lock.json
├─package.json
├─public
│ ├─favicon.ico
│ └─index.html
├─src
│ ├─App.vue
│ ├─api
│ │ ├─interface
│ │ │ ├─request
│ │ │ │ └─testRequest.ts
│ │ │ └─response
│ │ │ └─testResponse.ts
│ │ └─sampleName
│ │ ├─index.ts
│ │ └─testRepository.ts
│ ├─assets
│ │ ├─logo.png
│ │ └─main.scss
│ ├─components
│ │ ├─HelloWorld.vue
│ │ ├─SidebarComponent.vue
│ │ ├─TopComponent.vue
│ │ └─youtube-service
│ │ └─YoutubeHome.vue
│ ├─main.ts
│ ├─router
│ │ └─index.ts
│ ├─shims-vue.d.ts
│ └─views
│ ├─AboutView.vue
│ └─HomeView.vue
├─tsconfig.json
├─vue.config.js
└─yarn.lock
```
