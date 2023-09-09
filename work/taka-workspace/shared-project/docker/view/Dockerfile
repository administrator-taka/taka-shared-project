FROM node:lts-alpine

WORKDIR /app/my-vue-app

RUN apk update && \
    npm install -g npm @vue/cli && \
    yarn install

# RUN yarn install

# CMD ["yarn", "serve"]