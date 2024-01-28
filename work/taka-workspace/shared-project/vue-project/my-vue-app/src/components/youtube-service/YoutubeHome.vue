<template>
  <div>
    <Sidebar />
    <main class="main-content">
      <div>youtube home（仮）</div>
      <div>↓Java API疎通確認</div>
      <div>{{ result }}</div>
      <button @click="testVuex">Trigger Vuex</button>
    </main>
  </div>
</template>

<script>
import Sidebar from "@/components/SidebarComponent.vue";
import testRepository from "@/api/sampleName/testRepository";
import { ref, onMounted } from "vue";
import { useStore } from "vuex";

export default {
  components: {
    Sidebar,
  },
  setup() {
    const result = ref();
    const store = useStore();

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

    const testVuex = async () => {
      await store.dispatch("test/setUserDataAction", {
        username: "example",
        email: "example@example.com",
      });
      const userData = await store.dispatch("test/getUserData");
      console.log("Fetched User Data:", userData);
    };

    onMounted(() => {
      test();
    });

    return { result, testVuex };
  },
};
</script>

<style scoped></style>
