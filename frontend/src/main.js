import { createApp, VueElement } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css';
// import Bus from './eventbus.js';

createApp(App).use(router).use(router).mount('#app')
