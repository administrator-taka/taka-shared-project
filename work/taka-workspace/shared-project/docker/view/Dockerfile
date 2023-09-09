FROM node:lts-alpine

WORKDIR /app/my-vue-app

COPY . .

RUN apk update && \
    npm install -g npm @vue/cli && \
    yarn install
