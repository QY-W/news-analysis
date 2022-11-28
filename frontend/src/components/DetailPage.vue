<template>
<h1>This is Title:{{msg}}</h1>
<p>This is the contents</p>
</template>

<script>
//import {bus} from '../eventbus.js';

export default {
  name: "DetailPage",
  data() {
    return {
      msg:"placeholder"
    }
  },
  mounted() {
    // bus.$on("aMSG", (msg) => {
    //   this.msg = msg
    // })
  }
}
</script>

<style scoped>

</style>