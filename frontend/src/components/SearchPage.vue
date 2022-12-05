<template>
  <div class="search">
    <input type="text" v-model="searchText" placeholder="Type some text" />
    <!-- <span>Content: {{searchText}}</span> -->
  <h3>radio buttons</h3>
  <input type="radio" v-model="sortMethod" value="relevance" checked="checked">Relevance
  <input type="radio" v-model="sortMethod" value="newest">Newest
  <input type="radio" v-model="sortMethod" value="oldest">Oldest
  <br>
  <input type="checkbox" id="useTime"  v-model="boxChecked">
  <label > Filter time</label><br>

  From: 
  <input type="date" id="time-start" name="trip-start"
       value="1900-01-01">     
  To:
  <input type="date" id="time-end" name="trip-end"
       value="2022-12-09">

  <span>Sort Method: {{sortMethod}}</span>
  <br>
  <br>
    <button @click="searchNews">Submit</button>
    <!-- Result redender list -->
    <ol class="gradient-list" id="displayList">
    <li v-for="(r,id) in searchResult" :key = "id">
      <!-- <p>{{r}}</p> -->
      <h3>Title:{{r.webTitle}}</h3>
      <a :href = r.webUrl>Original Link</a>
      {{r.id}}
      <button @click="passID(r.id)" class="btn-detail" >See Details</button>
    </li>
    </ol>
  </div>
</template>

<script>
import axios from 'axios';
import router from '@/router/index.js'
import $ from 'jquery'
export default {
  name: "SearchPage",
  data() {
    return {
      sortMethod: "relevance",
      searchText: "content",
      searchResult: [],    
      std: {},
      boxChecked:false
    };
  },
  methods: {
    searchNews() {
      const path = '/api/search'
      this.std = {"sortMethod": this.sortMethod, "searchText":this.searchText, "filter":this.boxChecked,"from":String( $("#time-start").val()), "to":String( $("#time-end").val() ) }
      axios.post(path,this.std)
        .then((res) => {
          console.log("Loading Search")
          this.searchResult = res.data.searchResults;   
          console.log(this.searchResult)       
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log("Content failed to fetch")
          console.error(error);
        });
    },
    passID(someid) {
      this.id = someid;
      // bus.emit('toDetail', this.id);
      console.log("btn pressed "+this.id);
      // router.push('detail')
      router.push({
        path: 'detail',
        query: {
          id: this.id
        }
      })
    },
  }
}
// document.getElementById("time-end").valueAsDate = new Date();
</script>

<style scoped>
.search{
  width: 80%;
  margin-left:10% ;
}
.btn-detail {
  padding: 7px 18px;
  font-size: 18px;
  cursor: pointer;
  border-radius: 10px;
  border: none;
  background-color: #9ab4e4;
  transition: all 0.3s;
}
.btn-detail:hover {
  border-radius: 20px;
  /* color: var(--feedback-primary-color); */
  background-color:  #3972b2;
  background-image: url("data:image/svg+xml,%3Csvg width='52' height='26' viewBox='0 0 52 26' xmlns='http://www.w3.org/2000/svg'%3E%3Cg fill='none' fill-rule='evenodd'%3E%3Cg fill='%23ffacac' fill-opacity='0.4'%3E%3Cpath d='M10 10c0-2.21-1.79-4-4-4-3.314 0-6-2.686-6-6h2c0 2.21 1.79 4 4 4 3.314 0 6 2.686 6 6 0 2.21 1.79 4 4 4 3.314 0 6 2.686 6 6 0 2.21 1.79 4 4 4v2c-3.314 0-6-2.686-6-6 0-2.21-1.79-4-4-4-3.314 0-6-2.686-6-6zm25.464-1.95l8.486 8.486-1.414 1.414-8.486-8.486 1.414-1.414z' /%3E%3C/g%3E%3C/g%3E%3C/svg%3E");
  animation: animatedBackground 5s linear infinite alternate;
}

@keyframes animatedBackground {
  from {
    background-position: 0 0;
  }
  to {
    background-position: 100% 0;
  }
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