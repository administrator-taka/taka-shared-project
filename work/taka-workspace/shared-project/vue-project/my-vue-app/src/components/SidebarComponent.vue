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
export default {
  data() {
    return {
      sidebarLinks: [
        { name: "Home", routeName: "TopComponent" },
        { name: "Youtube Home", routeName: "YoutubeHome" },
        // 他のリンク情報をここに追加
      ],
    };
  },
  methods: {
    navigateTo(link) {
      const path = this.$router.resolve({ name: link.routeName }).href;
      console.log(`Navigating to ${link.name}, Path: ${path}`);
      this.$router.push({ name: link.routeName });
    },
  },
};
</script>

<style>
/* サイドバーのスタイルを追加 */
</style>
