<template>
  <div>
    <h1>TOP</h1>
    <!-- SidebarComponent.vue コンポーネントを使用 -->
    <Sidebar />
  </div>
</template>

<script>
import Sidebar from "./SidebarComponent.vue"; // SidebarComponent.vue をインポート

export default {
  components: {
    Sidebar, // コンポーネントを登録
  },
};
</script>

<style scoped>
/* 必要なスタイルを追加 */
</style>
