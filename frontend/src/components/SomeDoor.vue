<template>
    <div>
      <p>{{ msg }}</p>

      <div class="container">
        <button type="button" class="btn btn-primary">{{ msg }}</button>
        </div>
    </div>


  </template>
  
  <script>
import axios from 'axios';

export default {
  name: 'Door',
  data() {
    return {
      msg: '',
    };
  },
  methods: {
    getMessage() {
      const path = 'http://localhost:5000/open';
      axios.get(path)
        .then((res) => {
          this.msg = res.data;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
  },
  created() {
    this.getMessage();
  },
};
  </script>