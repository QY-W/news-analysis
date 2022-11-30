import { createApp, VueElement } from 'vue'
import App from './App.vue'
import router from './router'
import 'bootstrap/dist/css/bootstrap.css';
// import axios from 'axios';
// // import Bus from './eventbus.js';
// // import { apply } from 'core-js/fn/reflect';

// axios.defaults.headers.get['header-name'] = 'value'

createApp(App).use(router).use(router).mount('#app');
// App.all('*', function(req, res, next) {
//     res.header("Access-Control-Allow-Origin", "*");
//     res.header("Access-Control-Allow-Headers", "X-Requested-With,Content-Type");
//     res.header("Access-Control-Allow-Methods","PUT,POST,GET,DELETE,OPTIONS");
//     next();
// });
// using mitt to replace eventbus
// apply.config.globalProperties.$bus = mitt();