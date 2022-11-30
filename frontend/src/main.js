import { createApp, VueElement } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css';
// import Bus from './eventbus.js';
// import { apply } from 'core-js/fn/reflect';
// import mitt from "mitt";

createApp(App).use(router).use(router).mount('#app');
// using mitt to replace eventbus
// apply.config.globalProperties.$bus = mitt();