<template>
<h1 id="title">This is Title: default </h1>
<p>This is the contents</p>
</template>

<script>
//import {bus} from '../eventbus.js';
import bus from '@/bus/mittbus.js';

export default {
  name: "DetailPage",
  data() {
    return {
      // msg:"placeholder"
    }
  },
  mounted() {
    bus.on('toDetail', (data) => {
      console.log(data);
      //this.$refs.title.innerText = "213123123";
      document.getElementById("title").textContent = "ssss";
      

    })
    // bus.$on("aMSG", (msg) => {
    //   this.msg = msg
    // })
  }
}
</script>

<style scoped>

</style>