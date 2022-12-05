<template>
<div class = 'login'>
  <h2>Login</h2><br>
  <label for="text">Username:</label>
    <input type="text" v-model="loginUser" placeholder="Type some text" />
    <label for="lname">Password:</label>
    <input type="text" v-model="loginPW" placeholder="Type some text" /> 
    <button @click="tryLogin">Login</button>
<!--  -->
<br><br><br>
<h2>Register</h2><br>
<label for="text">Username:</label>
    <input type="text" v-model="regUser" placeholder="Type some text" />
    <label for="lname">Password:</label>
    <input type="text" v-model="regPW" placeholder="Type some text" /> 
    <button @click="tryReg">Register</button>
</div>



</template>

<script>
import axios from 'axios';
import $ from 'jquery'
// import VueWeather from "vue-weather-widget";
export default {

  name: "LoginPage",
  // components: {
  //     VueWeather,
  //   },
  data() {
    return {
      loginUser: "username",
      loginPW: "password",
      regUser: "new username",
      regPW: "new password",
      method: '',
      toSend: {},
      MSGState:0

    
    };
  },
  methods: {
    tryLogin() {
      this.method = "login"
      this.toSend = {
        "method": "login",
        "username": this.loginUser,
        "password": this.loginPW
      }
      this.sendMSG()
    },
    tryReg() {
      this.method = "register"
      this.toSend = {
        "method": "register",
        "username": this.regUser,
        "password": this.regPW
      }
      this.sendMSG()
    },
    sendMSG() {
      const path = '/api/login'
      axios.post(path,this.toSend)
        .then((res) => {
          console.log("Loading Search")
          this.MSGState = res.data.status;   
          console.log("status: " + res.data.status)
          console.log("Method: " + res.data.loginResults)     
          this.afterDB()
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log("Content failed to fetch")
          console.error(error);
        });
    },
      afterDB(){
        console.log(this.method, this.MSGState);
        if (this.method == 'login') {
          if ((this.MSGState == 0)) {
            alert("Login Fail");
          } else {
            document.getElementById("username-display").textContent = this.loginUser;
          }
        }else if (this.method == 'register') {
          if ((this.MSGState == 0)) {
            alert("register Fail, check syboml or name taken");
          } else {
            alert("register success, proceed to login");
          }
        }
        // this.MSGState == 0
    },

    },

    }
  

</script>

<style scoped>
  /* .login{
    padding: 1em,1em,1em,1em;
  } */
</style>