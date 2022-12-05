<template>
  <div id="app">
    <div id="wrapper">
    <div class="color-buttons">
          <button type="button" class="col-btn" id="col-btn1" value="c1">
            1
          </button>
          <button type="button" class="col-btn" id="col-btn2" value="c2">
            2
          </button>
          <button type="button" class="col-btn" id="col-btn3" value="c3">
            3
          </button>
          <button type="button" class="col-btn" value="cr">?</button>
        </div>


      <router-link to="/Home">Home</router-link> |
      <router-link to="/open">Connect</router-link> |
      <router-link to="/trending">Trending</router-link>|
      <router-link to="/login">Login</router-link> |
      <router-link to="/search">Search</router-link>
      <!-- <router-link to="/destination">destination</router-link> -->
      <div class = "flex">
        <p id = "username-display"> Guest</p>
        <button id = "btn-logout" @click="tryLogOut">Log Out</button>
      </div>

      <router-view/>
    </div>
  </div>
</template>

<script>
import $ from 'jquery'

export default {
  methods: {
    tryLogOut(){
      document.getElementById("username-display").textContent = "Guest";
    }
  },

}

let colorDic = {
        c1: "linear-gradient(to right, #1e0021c3, #f8731ac3)",
        c2: "linear-gradient(to right, #6d6d6dc3, #8a8a8ac3)",
        c3: "linear-gradient(to right, #fe2c2cc3, #2743f98b)",
      };
$(document).ready(function () {
        $("#col-btn1").css({ background: colorDic["c1"] });
        $("#col-btn2").css({ background: colorDic["c2"] });
        $("#col-btn3").css({ background: colorDic["c3"] });

        $(".col-btn").click(function () {
          //alert($(this).attr("value"));
          if ($(this).attr("value") == "cr") {
            let randomColor1 = Math.floor(Math.random() * 16777215).toString(
              16
            );
            let randomColor2 = Math.floor(Math.random() * 16777215).toString(
              16
            );
            let color =
              "linear-gradient(to right,#" +
              randomColor1 +
              ",#" +
              randomColor2 +
              ")";
            console.log(color);
            $("#wrapper").css({ background: color });
            return;
          }

          $("#wrapper").css({ background: colorDic[$(this).attr("value")] });
        });
      });
</script>

<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background: #EDF5E1;
}
#wrapper{
  min-height: 100vh;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
#username-display{
  text-align:left;
  padding-left: 1em;
  color: #2c3e50;
}
.flex{
  display: flex;
  justify-content: space-between;
}
#btn-logout{
  color: #2c3e50;
  border: none;
  border-radius: 12px;
  background-color: rgb(152, 170, 211);
  margin-right: 1em;
}
.color-buttons{
  text-align:right;
}

.color-buttons button {
        border: none;
        color: rgb(0, 0, 0);
        padding: 5px 12px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 12px;
        margin: 4px 2px;
        cursor: pointer;
        border-radius: 25px;
        
}
</style>
