<template>
<h1 id="title">This is Title: default </h1>
<p>This is the contents</p>
</template>

<script>
//import {bus} from '../eventbus.js';
import bus from '@/bus/mittbus.js';
// import { METHODS } from 'http';
import axios from 'axios';

export default {
  name: "DetailPage",
  data() {
    return {
      id:"placeholder"
    }
  },
  mounted() {
    // console.log(this.$route.query.id)
    document.getElementById("title").textContent = this.$route.query.id;
    this.id = this.$route.query.id;
    this.fetchDetailbyID()
    // checkDetail("this")

  },
  methods: {
    fetchDetailbyID() {
      const path = 'http://localhost:5000/detail';
      // const path = '/api/detail/';
      // axios.post(path,this.id)
      axios.post(path, this.id)
        .then((res) => {
          this.id = res.data.detailResults;
          console.log("ssssssssssssssssss")
          console.log(this.id)

        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log("EEEEEEEEEEEEE")
          console.error(error);
        });
    }
  },
}
</script>

<style scoped>

</style>