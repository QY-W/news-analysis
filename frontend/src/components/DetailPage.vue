<template>
  <h1 class = "preload-placeholder"> Loading</h1>
  <div class = 'detail'>
    <div class = 'container'> 
      <h1 id="title">This is Title: default </h1>
      <hr>
      <p id = "content" class = "content">Loading Contenting</p>
      <div id = "image-container">
        <!-- <img src="../assets/logo.png"> -->
        <img :src="require(`@/assets/${filename}.png`)">

      </div>
      <h2> {{sentiment}}</h2>
      <div class="count-list">
        <ul>
        <li v-for="(item,id) in wordcount" :key = "id" class="num" >
          <h3>{{item.count}}: {{item.word}}</h3>
        </li>

        </ul>
    </div>

    <button @click="openLDA()">See pyLDAvis Results</button>
    </div>
  </div>
</template>


<script>
//import {bus} from '../eventbus.js';
import bus from '@/bus/mittbus.js';
import $ from 'jquery'
// import html from  '@/assetslda.html';

import axios from 'axios';

export default {
  name: "DetailPage",
  data() {
    return {
      returnResult:'',
      id: "placeholder",
      author: '',
      title: '',
      content: 'cccc',
      filename: 'logo',
      wordcount: [{ word: 'Foo', count: 16 }, { message: 'Bar', count: 7 }], // [('doe', 15),('used', 10),('john', 10)]
      sentiment: '--',
      // html,
      // lda: "<h1 style='color:red'>Hello Gowtham</h1>"
    }
  },
  mounted() {
    // console.log(this.$route.query.id)
    // document.getElementById("title").textContent = this.$route.query.id;
    this.id = this.$route.query.id;
    this.fetchDetailbyID();
    // this.lda = require('@/assetslda.html').default
    //update
    // document.getElementById("content").textContent = this.content;


  },
  methods: {
    // fetch detail by ID
    fetchDetailbyID() {
      // const path = 'http://localhost:5000/detail';
      const path = '/api/detail'
      // axios.post(path,this.id)
      // axios.post(path, this.id)
      axios.post(path,this.id)
        .then((res) => {
          console.log("Loading Details")
          this.returnResult = res.data.detailResults;
          this.title = this.returnResult['webTitle']
          this.content = (this.returnResult['fields']['bodyText'])

          console.log("title is" + this.title)
          console.log("content is of type:" + typeof (this.content), (this.content.length))
          this.updateAfterFetch()

          // this.pic = res.data.wordcloud
          this.filename =  "wordcloud"  //res.data.filename
          console.log("cloud file name" + this.filename)

          // word count wordcount
          this.wordcount = res.data.wordcount;
          // sentimental score
          if (res.data.score > 0.2) {
            this.sentiment = 'Over All Sentiment: Positive'   //+ res.data.score
          } else if (res.data.score < -0.2) { 
            this.sentiment = 'Over All Sentiment: Negative'
          } else {
            this.sentiment = 'Over All Sentiment: Neutral'
          }
          $('.preload-placeholder').hide();
          $('.detail').show();

          
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log("Content failed to fetch")
          console.error(error);
        });
    },
    updateAfterFetch() {
      document.getElementById("title").textContent = this.title;
      document.getElementById("content").textContent = this.content;
    },
    openLDA() {
      window.open('lda.html')
// window.open(require('@/assetslda.html').default)//('file:///../assetslda.html');
    }
  },
}
</script>

<style scoped>
.detail{
  font-size: 1.5em;
  font-family: sans-serif;
  line-height: 1.6;
  display: none;
}
.container{
  width: 90%;
  word-wrap: break-word;
}

/* https://codepen.io/collincodes/pen/qYdxKp */

.count-list ul{
  /* text-align: center;
  display: inline-block; */
  columns: 2;
  -webkit-columns: 2;
  -moz-columns: 2;
}
.count-list .num {
  padding: 0.5rem 2rem;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  transition: 0.25s;
}
.count-list .num:before {
  /* content: "·"; */
  font-size: 4rem;
  font-weight: bold;
  color: #000;
  width: 2rem;
  opacity: 0.05;
  transition: 0.25s;
}

.count-list .num h3 {
  /* font-size: 2em; */
  position: relative;
  left: -1.5rem;
  color: #3d3d3d;
  transition: 0.25s;
  
}
.count-list .num:hover {
  background-color: #fafafa;
  cursor: pointer;
}
.count-list .num:hover:before {
  opacity: 0.2;
}
.count-list .num:hover h3 {
  left: 1rem;
}
</style>