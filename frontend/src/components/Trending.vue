<template>
  <div class="trending">
    <h1>{{ msg }}</h1>
    <h1>Trending News</h1>
    <ol class="gradient-list" id="displayList">
    <li>Lorem ipsum dolor sit amet, consectetur adipiscing elit.</li>
    <li v-for="(r,id) in trending" :key = "id">
      <!-- <p>{{r}}</p> -->
      <h3>Title:{{r.webTitle}}</h3>
      <!-- <p>Date:{{r.webPublicationDate}}</p> -->
      <a :href = r.webUrl>Original Link</a>
      {{r.id}}
      <button @click="sendToDetail()">Send to Detail</button>
    </li>
    </ol>
    <!-- <tr v-for = "r in resources" : key = "index">
      <td>{{r.id}}</td>
      <td>{{r.title}}</td>
    </tr> -->


  </div>
</template>

<script>
import axios from 'axios';
// import DetailPage from '../components/DetailPage.vue';
import {Bus} from '../eventbus.js';
export default {
  // components: { DetailPage },
  name: 'Trending',
  data() {
    return {
      trending: [],
    };
  },
  methods: {
    // sending to detail page
    // sendToDetail() {
    //   bus.$emit("aMSG", "MSG from trending")
    // },
    // getting from flask----------------
    getResources() {
      const path = 'http://localhost:5000/trending';
      axios.get(path)
        .then((res) => {
          this.trending = res.data.trendingResults;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getResources();
  },
  // getting from flask----------------
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

.trending{
  width: 80%;
  margin-left:10% ;
}

h3 {
  margin: 40px 0 0;
}

ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
  width: 100%;
}
a {
  color: #42b983;
}
/* https://codepen.io/erinesullivan/pen/qGrdGV */
ol.gradient-list {
  /* background: #dbd3b8b0; */
  counter-reset: gradient-counter;
  list-style: none;
  margin: 1.75rem 0;
  padding-left: 1rem;
  width: 100%;
}
ol.gradient-list > li {
  background: #acb1967d;;
  border-radius: 0 0.5rem 0.5rem 0.5rem;
  counter-increment: gradient-counter;
  margin-top: 1rem;
  min-height: 3rem;
  padding: 1rem 1rem 1rem 3rem;
  position: relative;
}
ol.gradient-list > li::before, ol.gradient-list > li {
  box-shadow: 0.25rem 0.25rem 0.6rem rgba(0, 0, 0, 0.05), 0 0.5rem 1.125rem rgba(75, 0, 0, 0.05);
}
ol.gradient-list > li::before, ol.gradient-list > li::after {
  background: linear-gradient(135deg, #83e4e2 0%, #a2ed56 100%);
  border-radius: 1rem 1rem 0 1rem;
  content: "";
  height: 3rem;
  left: -1rem;
  overflow: hidden;
  position: absolute;
  top: -1rem;
  width: 3rem;
}
ol.gradient-list > li::before {
  align-items: flex-end;
  content: counter(gradient-counter);
  color: #1d1f20;
  display: flex;
  font: 900 1.5em/1 "Montserrat";
  justify-content: flex-end;
  padding: 0.125em 0.25em;
  z-index: 1;
}

ol.gradient-list > li + li {
  margin-top: 2rem;
  
}
</style>
