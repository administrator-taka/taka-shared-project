const { defineConfig } = require("@vue/cli-service");

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
        target: "http://localhost:8080",
        // target: "http://host.docker.internal:8080",
        changeOrigin: true,
        pathRewrite: {
          "^/api": "",
        },
      },
    },
  },
});
