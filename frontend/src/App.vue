<template>
  <div id="app">
    <router-link to="/Home">Home</router-link> |
    <router-link to="/open">Open</router-link> |
    <router-link to="/trending">Trending</router-link>|
    <router-link to="/detail">Detail</router-link>
    <router-view/>
  </div>
</template>

<style>

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  background: #EDF5E1;

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
</style>
