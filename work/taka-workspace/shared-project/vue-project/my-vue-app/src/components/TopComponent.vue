<template>
  <div>
    <Sidebar />
    <main>
      <div>トップ画面</div>
    </main>
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
