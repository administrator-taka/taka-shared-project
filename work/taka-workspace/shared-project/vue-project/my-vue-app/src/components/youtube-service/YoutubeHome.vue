<template>
  <div>
    <Sidebar />
    <main class="main-content">
      <div>youtube home（仮）</div>
    </main>
  </div>
</template>

<script>
import Sidebar from "@/components/SidebarComponent.vue"; // SidebarComponent.vue をインポート
import testRepository from "@/api/sampleName/testRepository";
export default {
  components: {
    Sidebar, // コンポーネントを登録
  },
  setup(){
    const test=async ()=>{
      testRepository.testApi(
          {'test':'test_name_a'}).then((res)=>{

        console.log("★★★api疎通確認★★★")
        console.log(res
        )
      }).catch((error)=>{
        console.log("★★★エラー動作確認★★★")
        console.log(error)
      })
    }
    test()
    return {}
  }
};
</script>

<style scoped></style>
