# 使用するNode.jsのバージョンを指定
FROM node:18.17.1-alpine

# 作業ディレクトリを設定
WORKDIR /app/my-vue-app

# 必要なパッケージをインストール
RUN apk update && \
    npm install -g npm && \
    npm install -g @vue/cli && \
    yarn install

# # コンテナ内でアプリケーションを実行
# CMD ["yarn", "serve"]
