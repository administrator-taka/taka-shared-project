<template>
  <div>
    <h2>Sidebar</h2>
    <ul>
      <li
        v-for="link in sidebarLinks"
        :key="link.name"
        @click="navigateTo(link)"
      >
        {{ link.name }}
      </li>
    </ul>
  </div>
</template>

<script>
import { ref } from "vue";

export default {
  setup() {
    // data()からsetup()に移行したデータ
    const sidebarLinks = ref([
      { name: "Home", routeName: "TopComponent" },
      { name: "Youtube Home", routeName: "YoutubeHome" },
      // 他のリンク情報をここに追加
    ]);

    // setup()内で返すデータとメソッドを定義
    const navigateTo = (link) => {
      const path = this.$router.resolve({ name: link.routeName }).href;
      console.log(`Navigating to ${link.name}, Path: ${path}`);
      this.$router.push({ name: link.routeName });
    };

    // setup()からエクスポート
    return {
      sidebarLinks,
      navigateTo,
    };
  },
};
</script>

<style>
/* サイドバーのスタイルを追加 */
</style>
