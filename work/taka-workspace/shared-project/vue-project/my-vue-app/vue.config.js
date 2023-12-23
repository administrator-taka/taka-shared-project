const { defineConfig } = require("@vue/cli-service");
const apiUrl = process.env.API_DOMAIN;

module.exports = defineConfig({
  transpileDependencies: true,
  configureWebpack: {
    resolve: {
      alias: {
        axios: "axios",
      },
    },
  },
  devServer: {
    port: 3000,
    proxy: {
      "/api": {
        target: apiUrl,
        changeOrigin: true,
        pathRewrite: {
          "^/api": "",
        },
      },
    },
  },
});
