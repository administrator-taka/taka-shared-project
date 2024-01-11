<template>
  <div>
    <Sidebar />
    <main class="main-content">
      <div>youtube home（仮）</div>
      <div>↓Java API疎通確認</div>
      <div>{{ result }}</div>
    </main>
  </div>
</template>

<script>
import Sidebar from "@/components/SidebarComponent.vue"; // SidebarComponent.vue をインポート
import testRepository from "@/api/sampleName/testRepository";
import { ref } from "vue";

export default {
  components: {
    Sidebar, // コンポーネントを登録
  },
  setup() {
    const result = ref();
    const test = async () => {
      testRepository
        .testApi({ test: "test_name_a" })
        .then((res) => {
          console.log("★★★api疎通確認★★★");
          console.log(res);
          result.value = res;
        })
        .catch((error) => {
          console.log("★★★エラー動作確認★★★");
          console.log(error);
        });
    };
    test();
    return { result };
  },
};
</script>

<style scoped></style>
