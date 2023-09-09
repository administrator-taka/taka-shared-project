# 使用するNode.jsのバージョンを指定
FROM node:14.17.0-alpine

# 作業ディレクトリを設定
WORKDIR /app/my-vue-app

# npmおよびYarnのバージョンアップデートとVue CLIのインストール
RUN apk update && \
apk add --no-cache yarn && \
    npm install -g npm@6.14.18 && \
    npm install -g @vue/cli@4.5.13 && \
    npm install -g serve

# プロジェクトの依存関係をインストール
RUN yarn install

# コンテナ内でアプリケーションを実行
CMD ["yarn", "serve"]
