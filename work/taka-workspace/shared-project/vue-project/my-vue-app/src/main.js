import { createApp } from 'vue'
import App from './App.vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap/dist/js/bootstrap.min.js'
import router from './router' // router.js をインポート

createApp(App)
  .use(router) // Vue Routerをアプリケーションに統合
  .mount('#app')
